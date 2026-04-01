python   
import akshare as ak
import json
import os
 
# 获取指数估值数据
index_valuation_df = ak.index_value_a_stock()
 
# 保存为 JSON
data = index_valuation_df.to_dict(orient="records")
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
 
print("更新完成")
 
