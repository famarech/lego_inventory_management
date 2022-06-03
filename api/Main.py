import bricklink_api

# json_obj = bricklink_api.catalog_item.get_price_guide("Set", "6335-1", new_or_used="U")
#
# print(json_obj['data']['avg_price'])
#
#
# 3005
# 11

json_obj = bricklink_api.catalog_item.get_price_guide("Part", "3005", color_id="11", new_or_used="U")
print(json_obj['data']['avg_price'])


# for i in json_obj['data']['avg_price']:
#     print(i)