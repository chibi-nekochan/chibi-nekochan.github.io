# ちび猫ちゃん公式サイト

https://chibi-nekochan.github.io/

静的HTML・CSSで構成した公式サイト。Creator: たまごぼーろ。

## 更新

`site.json` のURL、説明文、SNSリンクを編集し、Python 3で `python3 build.py` を実行します。生成された `index.html`、`robots.txt`、`sitemap.xml` と変更した素材を一緒にコミットしてください。GitHub Pagesはmainブランチのルートから公開します。

## 独自ドメインへの移行

1. GitHubの案内に沿ってドメインを検証し、DNSとPagesのCustom domainを設定します。
2. `site.json` の `url` をHTTPSの新しいドメインに変更して再生成します。canonical、OGP、サイトマップのURLが一括で変わります。
3. HTTPSを確認し、SNSのリンクとSearch Consoleの登録・サイトマップを更新します。

## 検索への登録

公開後、Google Search ConsoleにURLプレフィックスで登録し、指定された確認用HTMLまたはメタタグで所有権を確認します。その後 `sitemap.xml` を送信し、トップページのインデックス登録をリクエストします。検索への掲載時期や順位は保証されません。

## 画像

`character-design.png` は提供されたキャラクターデザイン原本です。`character-portrait.png` と `og.png` は原本を参照して画像生成で制作したWeb用素材です。キャラクターと画像の再利用ライセンスは付与していません。
