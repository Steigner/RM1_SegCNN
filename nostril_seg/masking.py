import os
import json
import cv2
import numpy as np


class Masking(object):
    def __init__(self):
        self.width = 640
        self.height = 480

        # 9s0,45s0,48s0,62s0
        self.json_path = "JSON/json1-40.json"
        self.file_bbs = {}

        self.input_dir = "test_dataset/images/"
        self.target_dir = "test_dataset/masks/"

        self.data = self.__open_json(self.json_path)

    def __open_json(self, json_path):
        # Read JSON file
        with open(json_path) as f:
            return json.load(f)

    # Extract X and Y coordinates if available and update dictionary
    def __add_to_dict(self, data, itr, key, count):
        try:
            x_points = data[itr]["regions"][str(count)]["shape_attributes"][
                "all_points_x"
            ]
            y_points = data[itr]["regions"][str(count)]["shape_attributes"][
                "all_points_y"
            ]

        except:
            print("Skipping", key)
            return

        all_points = []
        for i, x in enumerate(x_points):
            all_points.append([x, y_points[i]])

        self.file_bbs[key] = all_points

    def mask_process(self):
        data = self.data
        count = 0

        for itr in data:
            file_name_json = data[itr]["filename"]
            # Contains count of masks for a single ground truth image
            sub_count = 0

            if len(data[itr]["regions"]) > 1:
                for _ in range(len(data[itr]["regions"])):
                    key = file_name_json[:-4] + "*" + str(sub_count + 1)
                    self.__add_to_dict(data, itr, key, sub_count)
                    sub_count += 1
            else:
                self.__add_to_dict(data, itr, file_name_json[:-4], 0)

        am = []
        for itr in self.file_bbs:
            num_masks = itr.split("*")

            mask = np.ones((self.height, self.width)) * 2

            try:
                arr = np.array(self.file_bbs[itr])
            except:
                print("Not found:", itr)
                continue

            count += 1

            am.append(arr)

            if len(num_masks) == 1:
                cv2.imwrite(os.path.join(self.target_dir, num_masks[0] + ".png"), mask)

            else:
                if num_masks[1] == "1":
                    unify = cv2.fillPoly(mask, [np.int32(am[0])], color=(1))
                    # cv2.imwrite(os.path.join("test/masks", num_masks[0] + ".png") , unify)

                if num_masks[1] == "2":
                    unify = cv2.fillPoly(unify, [np.int32(am[1])], color=(3))
                    cv2.imwrite(
                        os.path.join(self.target_dir, num_masks[0] + ".png"), unify
                    )
                    am = []


if __name__ == "__main__":
    m = Masking()
    m.mask_process()
