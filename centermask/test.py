reg_tragets=[[1,2,3,4]]
left_right = [1,3]
top_bottom = [2,4]
centerness = (left_right.min(dim=-1)[0] / left_right.max(dim=-1)[0]) * \
              (top_bottom.min(dim=-1)[0] / top_bottom.max(dim=-1)[0])
print(centerness)