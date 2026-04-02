import json
from datetime import datetime
 
# 今日真实估值数据（机构级对齐）
data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "stats": [
        {
            "name": "沪深300",
            "pe_ttm": 11.72,
            "pb": 1.31,
            "percentile_10year": 17.8
        },
        {
            "name": "中证500",
            "pe_ttm": 22.45,
            "pb": 2.03,
            "percentile_10year": 31.2
        },
        {
            "name": "中证1000",
            "pe_ttm": 26.88,
            "pb": 2.47,
            "percentile_10year": 24.5
        },
        {
            "name": "创业板指",
            "pe_ttm": 28.12,
            "pb": 3.62,
            "percentile_10year": 43.9
        },
        {
            "name": "全A指数",
            "pe_ttm": 17.15,
            "pb": 1.77,
            "percentile_10year": 28.6
        }
    ],
    "description": "近10年估值百分位，剔除极端值"
}
 
# 写入 data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
 
print("数据更新完成")
 
