import numpy as np
import open3d as o3d

data = np.load("EXPORT_BBOX_AND_CAMS_ONLY.npz")

print(f"data[xyz_min] = {data['xyz_min']}")
print(f"data[xyz_max] = {data['xyz_max']}")
print(f"data[cam_lst] = {data['cam_lst']}")

bbox_min = [ x for x in data['xyz_min'] ]
bbox_max = [ x for x in data['xyz_max'] ]
bbox_lines = o3d.geometry.LineSet.create_from_oriented_bounding_box(
    o3d.geometry.AxisAlignedBoundingBox(min_bound=bbox_min, max_bound=bbox_max)
)

cam_lst = data['cam_lst']

camera_frames = []
for cam_info in cam_lst:
    cam_o, cam_d = cam_info[0], cam_info[1:]
    camera_frames = o3d.geometry.TriangleMesh.create_oordinate_frame(size = 0.1)
    camera_frames.translate(cam_o)
    camera_frames.append(cam_d)

vis = o3d.visualization.Visualizer()
vis.create_window()

vis.add_geometry(bbox_lines)
for frame in camera_frames:
    vis.add_geometry(frame)

vis.run()
vis.destroy_window()