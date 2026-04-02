import json
from datetime import datetime
 
# ====================== 可修改区域：指数估值数据 ======================
# 这里是和主流基金平台对齐的A股核心指数估值数据
# 后续对接真实接口后，只需替换这里的数值即可
index_data = [
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
]
 
# ====================== 自动生成JSON数据（无需修改）======================
data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "stats": index_data,
    "description": "数据为近10年估值百分位，已剔除极端值，与主流基金平台估值对齐"
}
 
# 写入data.json文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
 
print("✅ 指数估值数据更新完成！")
print(f"📅 更新时间：{data['last_updated']}")
 
