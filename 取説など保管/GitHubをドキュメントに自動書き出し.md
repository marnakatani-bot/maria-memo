# GitHubマリアメモ → Googleドキュメント 自GitHubをドキュメントに自動書き出し動書き出し

## 何をしたか

GitHubに保存されているマリアメモ（Markdownファイル）を、Google Apps Scriptを使って一括でGoogleドキュメントに書き出した。

## 仕組み

1. **GitHub API** でリポジトリのファイル一覧を取得
2. すべてのフォルダを再帰的に探索し、`.md`ファイルを収集
3. 各ファイルの内容を取得してGoogleドキュメントとして作成
4. Googleドライブに「マリアメモ_日付」フォルダをつくり、まとめて保存

## 使ったもの

- **Google Apps Script**（無料・インストール不要）
- **GitHub Personal Access Token**（認証用・無料）

## 再実行したいとき

1. [script.google.com](https://script.google.com) を開く
2. このプロジェクトを選ぶ
3. ▶ 実行を押すだけ

## 注意

- トークンは他人に見せない
- トークンには有効期限なしを設定済み