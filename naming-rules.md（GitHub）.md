# maria-memo 命名ルール

**ファイル名：** `命名ルール.md`（Obsidian）／ `naming-rules.md`（GitHub）
**作成日：** 2026-04-29

---

## 方針

- **GitHub**：英語スラグ（URLエンコード問題を回避）
- **Obsidian**：日本語タイトル（`title:` frontmatterで管理）
- 紐づけは frontmatter の `github_slug` 項目で一元管理

---

## GitHubスラグのルール

- 英小文字 + ハイフン区切り
- バージョンは末尾に付ける：`-v1`、`-v2`
- カテゴリプレフィックス：

| カテゴリ | フォルダ | スラグ例 |
|---------|---------|---------|
| 理論 | 理論/ | `usapyon-theory-v1.md` |
| 記事 | 記事/ | `substack-9yen-universe.md` |
| SNS | SNS/ | `sns-bluesky-20260422.md` |
| 対話 | 対話/ | `talk-geo-insight-01.md` |
| ひらめき | inspiration/ | `idea-tetrachromacy.md` |

---

## Obsidian Frontmatter テンプレート

```yaml
---
title: うさぴょん理論：空間と粒子の動態
github_slug: usapyon-theory-v1
category: 理論
tags: [布理論, 次元マッピング, 空間モデル]
created: 2026-04-22
status: draft
---
```

## 今回の適用例

| GitHub ファイル名 | Obsidian title |
|----------------|---------------|
| `usapyon-theory-v1.md` | うさぴょん理論：空間と粒子の動態 |
| `funo-theory-v1.md` | 布理論：素材の質感と情報定着 |
| `funo-usapyon-v2.md` | 布理論×うさぴょん理論 V2.0 |
| `substack-9yen-universe.md` | 残高9円から宇宙が動き出した |