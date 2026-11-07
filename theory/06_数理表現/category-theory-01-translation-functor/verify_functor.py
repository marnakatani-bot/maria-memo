"""圏論のはじまり：翻訳で変わるものと残るもの

英語の圏から日本語の圏への「翻訳」が関手になっているかを確かめる。
矢印の意味は「左のものが、右のものとして現れる」。

実行: python3 verify_functor.py
"""

# 圏 = 対象の集まり + 矢印（名前: (始まり, 終わり)）
english = {
    "objects": {"Being", "Doing"},
    "arrows": {"f": ("Being", "Doing")},
}

japanese = {
    "objects": {"在り方", "行い", "佇まい"},
    "arrows": {
        "g": ("在り方", "行い"),
        "h": ("在り方", "佇まい"),
    },
}

# 翻訳 = 対象を対象へ、矢印を矢印へ写す
translate_objects = {"Being": "在り方", "Doing": "行い"}
translate_arrows = {"f": "g"}


def is_functor(src, dst, obj_map, arr_map):
    """矢印の始まりと終わりが、写した先でも一致するか（上の道と下の道が同じ所に着くか）"""
    ok = True
    for name, (start, end) in src["arrows"].items():
        image = arr_map[name]
        image_start, image_end = dst["arrows"][image]
        same = (obj_map[start], obj_map[end]) == (image_start, image_end)
        print(f"  {name}: {start}→{end}  を写すと  {image}: {image_start}→{image_end}  … {'一致' if same else '不一致'}")
        ok = ok and same
    return ok


def unreached_arrows(dst, arr_map):
    """写ってこない矢印（ニュアンスの居場所）"""
    reached = set(arr_map.values())
    return {n: a for n, a in dst["arrows"].items() if n not in reached}


print("1. 翻訳は関手か")
print("  → 関手です" if is_functor(english, japanese, translate_objects, translate_arrows) else "  → 関手ではありません")

print("\n2. 英語の圏から写ってこない矢印")
for name, (start, end) in unreached_arrows(japanese, translate_arrows).items():
    print(f"  {name}: {start}→{end}")
