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
social_icons = {'X':'𝕏', 'YouTube':'▶', 'TikTok':'♪'}
links = ''.join(f'<a class="button social-icon" href="{e(s["url"])}" aria-label="{e(s["label"])}を開く"><span aria-hidden="true">{social_icons.get(s["label"], e(s["label"]))}</span></a>' for s in socials)
social_section = f'<section class="social wrap" id="social"><p class="eyebrow">FOLLOW</p><h2>ちび猫ちゃんは、<br>たまごぼーろのSNSで活躍中。</h2><p>日々の投稿や動画で、ちび猫ちゃんに会えます。</p><div class="social-links">{links}</div></section>' if socials else ''
schema = {'@context':'https://schema.org','@type':'WebSite','name':c['name']+'公式サイト','alternateName':c['englishName'],'url':url+'/','inLanguage':'ja','description':c['description']}
html = f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(c['description'])}"><link rel="canonical" href="{e(url)}/">
<meta property="og:type" content="website"><meta property="og:locale" content="ja_JP"><meta property="og:site_name" content="ちび猫ちゃん"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(c['description'])}"><meta property="og:url" content="{e(url)}/">{meta_image}<meta name="twitter:card" content="{'summary_large_image' if og else 'summary'}"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(c['description'])}"><meta name="theme-color" content="#e7f1f8">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style-social.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace('<','&#60;')}</script></head>
<body><a class="skip" href="#main">本文へ移動</a><div class="wrap"><header><a class="brand" href="./">ちび猫ちゃん<span aria-hidden="true">🐾</span></a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-menu"><span class="menu-icon" aria-hidden="true"></span><span class="sr-only">メニューを開く</span></button><nav id="main-menu" aria-label="メインメニュー"><a href="#about">紹介</a><a href="#charm">魅力</a>{'<a href="#social">SNS</a>' if socials else ''}</nav></header>
</div><main id="main"><div class="wrap"><section class="hero {'text-only' if not image else ''}"><div><p class="eyebrow">OFFICIAL WEBSITE</p><h1>ちび猫ちゃん🐾</h1><p class="english">CHIBI NEKOCHAN</p><p class="intro">ちいさな、ねこちゃんのような女の子。<br>いつも一緒にいたくなる、<br>やさしくて甘えんぼうなマスコット。</p><a class="button" href="#about">ちび猫ちゃんについて</a></div>{portrait}</section></div>
<section class="about" id="about"><img class="about-character" src="character-portrait.png" alt="" aria-hidden="true"><div class="wrap section-grid"><div><p class="eyebrow">ABOUT</p><h2>ちび猫ちゃんについて</h2></div><div class="about-copy"><p class="about-lead">ちいさな、ねこちゃんの<span class="mobile-break"><br></span>ような女の子。</p><p>銀青のボブに白いねこ耳、<br>きらきらした青い瞳。</p><p>赤いリボンとピンクのワンピースが<br>ちび猫ちゃんのトレードマークです。</p><p>好奇心いっぱいで、ちょっぴり不器用。<br>がんばってみたり、転んでみたり、<br>ときどき小さな事件を起こしてみたり。</p><p>言葉は少なくても、<br>表情やしぐさで気持ちを伝えてくれます。</p><p class="about-final">いつもの一日に、<br>ほんの少しだけ「かわいい」を増やしてくれる。</p><p class="about-final">それが、ちび猫ちゃんです。</p></div></div></section><section class="charm wrap" id="charm"><div class="charm-heading"><p class="eyebrow">LITTLE MOMENTS</p><h2>ちいさな表情に、きゅん。</h2><p>にっこりしたり、びっくりしたり。<br>どんな顔も、そばで見ていたくなる。</p></div><div class="charm-grid"><article class="charm-card"><button class="image-open" type="button" data-image="smile.png" data-alt="目を細めてにっこり笑うちび猫ちゃん" aria-label="笑顔のちび猫ちゃんを大きく見る"><img src="smile.png" width="1024" height="1024" alt="目を細めてにっこり笑うちび猫ちゃん" loading="lazy"></button><div class="charm-copy"><span class="moment">01 / SMILE</span><h3>つられて、にっこり。</h3><p>目をきゅっと細めた、うれしい笑顔。<br>見ているこっちまで、ほっぺがゆるむ。</p></div></article><article class="charm-card"><button class="image-open" type="button" data-image="surprise.png" data-alt="青い瞳をまんまるにしてびっくりするちび猫ちゃん" aria-label="びっくり顔のちび猫ちゃんを大きく見る"><img src="surprise.png" width="1024" height="1024" alt="青い瞳をまんまるにしてびっくりするちび猫ちゃん" loading="lazy"></button><div class="charm-copy"><span class="moment">02 / SURPRISE</span><h3>あれっ？ なあに？</h3><p>まんまるな青い瞳に、小さなおくち。<br>びっくりした顔にも、きゅん。</p></div></article><article class="charm-card"><button class="image-open" type="button" data-image="palms.png" data-alt="両手のひらにちょこんと座る小さなちび猫ちゃん" aria-label="手のひらに座るちび猫ちゃんを大きく見る"><img src="palms.png" width="1024" height="1024" alt="両手のひらにちょこんと座る小さなちび猫ちゃん" loading="lazy"></button><div class="charm-copy"><span class="moment">03 / TOGETHER</span><h3>この手のひらが、特等席。</h3><p>約12cmの、ちいさなちいさな存在。<br>そっと包んで、ずっと一緒に。</p></div></article></div></section>{social_section}</main>
<dialog class="image-dialog" aria-label="画像を拡大表示"><button class="dialog-close" type="button" aria-label="拡大表示を閉じる">×</button><img src="" alt=""></dialog><script>const menuButton=document.querySelector('.menu-toggle');const menu=document.querySelector('#main-menu');menuButton.addEventListener('click',()=>{{const open=menuButton.getAttribute('aria-expanded')==='true';menuButton.setAttribute('aria-expanded',String(!open));menu.classList.toggle('is-open',!open);menuButton.querySelector('.sr-only').textContent=open?'メニューを開く':'メニューを閉じる'}});menu.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{{menuButton.setAttribute('aria-expanded','false');menu.classList.remove('is-open');menuButton.querySelector('.sr-only').textContent='メニューを開く'}}));const dialog=document.querySelector('.image-dialog');const dialogImage=dialog.querySelector('img');document.querySelectorAll('.image-open').forEach(button=>button.addEventListener('click',()=>{{dialogImage.src=button.dataset.image;dialogImage.alt=button.dataset.alt;dialog.showModal()}}));dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',event=>{{if(event.target===dialog)dialog.close()}});</script><div class="wrap"><section class="creator" aria-label="クリエイター"><p><small>Creator</small><br>たまごぼーろ</p><p class="english">CHIBI NEKOCHAN<br>OFFICIAL WEBSITE</p></section><footer>© ちび猫ちゃん</footer></div></body></html>'''
(root/'index.html').write_text(html)
(root/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {url}/sitemap.xml\n')
(root/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{e(url)}/</loc></url></urlset>')
(root/'.nojekyll').touch()
print('Generated index.html, robots.txt, sitemap.xml')
