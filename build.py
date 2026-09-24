"""Generate the static site. Update site.json when changing the domain or links."""
from pathlib import Path
from html import escape as e
import json

root = Path(__file__).resolve().parent
c = json.loads((root / 'site.json').read_text())
url = c['url'].rstrip('/')
title = c['name'] + ' | 公式サイト'
image = c.get('hero')
og = c.get('ogImage')
socials = c['socials']
for s in socials:
    assert s['url'].startswith('https://'), 'SNS links must use HTTPS'
for asset in [image, og]:
    if asset:
        assert (root / asset).is_file(), f'Missing asset: {asset}'
meta_image = f'<meta property="og:image" content="{e(url + "/" + og)}"><meta name="twitter:image" content="{e(url + "/" + og)}"><meta property="og:image:alt" content="ちび猫ちゃん">' if og else ''
portrait = f'<div class="portrait"><img src="{e(image)}" alt="銀青のボブ、白いねこ耳、ピンクのワンピース姿のちび猫ちゃん" width="1024" height="1536" fetchpriority="high"></div>' if image else ''
links = ''.join(f'<a class="button" href="{e(s["url"])}" >{e(s["label"])}</a>' for s in socials)
social_section = f'<section class="social wrap" id="social"><p class="eyebrow">FOLLOW</p><h2>もっと、ちび猫ちゃん。</h2><p>日々の投稿や動画は、こちらから。</p><div class="social-links">{links}</div></section>' if socials else ''
schema = {'@context':'https://schema.org','@type':'WebSite','name':c['name']+'公式サイト','alternateName':c['englishName'],'url':url+'/','inLanguage':'ja','description':c['description']}
html = f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(c['description'])}"><link rel="canonical" href="{e(url)}/">
<meta property="og:type" content="website"><meta property="og:locale" content="ja_JP"><meta property="og:site_name" content="ちび猫ちゃん"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(c['description'])}"><meta property="og:url" content="{e(url)}/">{meta_image}<meta name="twitter:card" content="{'summary_large_image' if og else 'summary'}"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(c['description'])}"><meta name="theme-color" content="#e7f1f8">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace('<','&#60;')}</script></head>
<body><a class="skip" href="#main">本文へ移動</a><div class="wrap"><header><a class="brand" href="./">ちび猫ちゃん</a><nav aria-label="メインメニュー"><a href="#about">紹介</a><a href="#design">デザイン</a>{'<a href="#social">SNS</a>' if socials else ''}</nav></header>
</div><main id="main"><div class="wrap"><section class="hero {'text-only' if not image else ''}"><div><p class="eyebrow">OFFICIAL WEBSITE</p><h1>ちび猫ちゃん</h1><p class="english">CHIBI NEKOCHAN</p><p class="intro">ちいさな、ねこちゃんのような女の子。<br>いつも一緒にいたくなる、<br>やさしくて甘えんぼうなマスコット。</p><a class="button" href="#about">ちび猫ちゃんについて</a></div>{portrait}</section></div>
<section class="about" id="about"><div class="wrap section-grid"><div><p class="eyebrow">ABOUT</p><h2>ちび猫ちゃんについて</h2></div><div><p class="about-lead">手のひらに、ちょこん。</p><p>ちび猫ちゃんは、身長約12cmのオリジナルキャラクター。<br>銀青のボブと白いねこ耳、きらきらした青い瞳が目印です。</p><p>大きな胸リボンに、白いフリルのピンクのワンピース。<br>青いしっぽと、はだしの小さな足もチャームポイント。</p><dl class="profile"><div><dt>サイズ</dt><dd>約12cm・手のひらサイズ</dd></div><div><dt>性格</dt><dd>やさしくて甘えんぼう</dd></div></dl></div></div></section><section class="design wrap" id="design"><div class="section-heading"><div><p class="eyebrow">CHARACTER DESIGN</p><h2>いろんな角度から。</h2></div><p>すがたも、表情も。<br>ちび猫ちゃんをご紹介。</p></div><a class="design-image" href="character-design.png" aria-label="キャラクターデザインを原寸で開く"><img src="character-design.png" width="1055" height="1491" alt="ちび猫ちゃんの正面・背面・側面、4つの表情、カラーパレットと約12cmのサイズ感をまとめたキャラクターデザイン" loading="lazy"></a><p class="image-note">画像をタップすると大きく表示できます。</p></section>{social_section}</main>
<div class="wrap"><section class="creator" aria-label="クリエイター"><p><small>Creator</small><br>たまごぼーろ</p><p class="english">CHIBI NEKOCHAN<br>OFFICIAL WEBSITE</p></section><footer>© ちび猫ちゃん</footer></div></body></html>'''
(root/'index.html').write_text(html)
(root/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {url}/sitemap.xml\n')
(root/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{e(url)}/</loc></url></urlset>')
(root/'.nojekyll').touch()
print('Generated index.html, robots.txt, sitemap.xml')
