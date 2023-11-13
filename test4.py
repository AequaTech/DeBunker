import json

import requests
import bs4
import requests

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

text='''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="3_uHMeg4gGqsOJBpUed_y3JTspEoeXAIroaP56Qbw7c"/>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-W001DSB1QT"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() {
        dataLayer.push(arguments);
    }
    gtag('js', new Date());

    gtag('config', 'G-W001DSB1QT');
    </script>
    <title>The Black List: la lista nera del web - Bufale</title>
    <link rel="stylesheet" id="swiper-css" href="https://www.bufale.net/wp-content/themes/bufale/lib/swiper/swiper.min.css?ver=4.0" type="text/css" media="all">
    <script type="text/javascript" src="https://www.bufale.net/wp-content/themes/bufale/lib/swiper/swiper.min.js?ver=4.0" id="swiper-js"></script>
    <link rel="stylesheet" id="font-awesome-css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css?ver=4.2.0" type="text/css" media="all">
    <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'/>

    <!-- Google Tag Manager for WordPress by gtm4wp.com -->
    <script data-cfasync="false" data-pagespeed-no-defer>
    var gtm4wp_datalayer_name = "dataLayer";
    var dataLayer = dataLayer || [];
    </script>
    <!-- End Google Tag Manager for WordPress by gtm4wp.com -->
    <!-- This site is optimized with the Yoast SEO plugin v16.4 - https://yoast.com/wordpress/plugins/seo/ -->
    <link rel="canonical" href="https://www.bufale.net/the-black-list-la-lista-nera-del-web/"/>
    <meta property="og:locale" content="it_IT"/>
    <meta property="og:type" content="article"/>
    <meta property="og:title" content="The Black List: la lista nera del web - Bufale"/>
    <meta property="og:description" content="Come promesso, in aggiornamento Black List e add-on. I siti che per più di un anno non abbiano pubblicato bufale o fatto disinformazione potranno essere rimossi come forma di incentivo positivo e critico, mentre le finte testate giornalistiche rimarranno dentro. Aspettiamo come sempre un vostro riscontro in merito, per poter di conseguenza migliorare il nostro [&hellip;]"/>
    <meta property="og:url" content="https://www.bufale.net/the-black-list-la-lista-nera-del-web/"/>
    <meta property="og:site_name" content="Bufale"/>
    <meta property="article:modified_time" content="2022-11-22T16:59:42+00:00"/>
    <meta property="og:image" content="https://www.bufale.net/wp-content/uploads/sites/5/2016/01/blacklist.jpg"/>
    <meta property="og:image:width" content="1200"/>
    <meta property="og:image:height" content="630"/>
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:label1" content="Est. reading time"/>
    <meta name="twitter:data1" content="4 minuti"/>
    <!-- / Yoast SEO plugin. -->

    <link rel='dns-prefetch' href='//stats.wp.com'/>
    <script type="text/javascript">
    /* <![CDATA[ */
    window._wpemojiSettings = {
        "baseUrl": "https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/72x72\/",
        "ext": ".png",
        "svgUrl": "https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/svg\/",
        "svgExt": ".svg",
        "source": {
            "concatemoji": "https:\/\/www.bufale.net\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.4.1"
        }
    };
    /*! This file is auto-generated */
    !function(i, n) {
        var o,
            s,
            e;
        function c(e) {
            try {
                var t = {
                    supportTests: e,
                    timestamp: (new Date).valueOf()
                };
                sessionStorage.setItem(o, JSON.stringify(t))
            } catch (e) {}
        }
        function p(e, t, n) {
            e.clearRect(0, 0, e.canvas.width, e.canvas.height),
            e.fillText(t, 0, 0);
            var t = new Uint32Array(e.getImageData(0, 0, e.canvas.width, e.canvas.height).data),
                r = (e.clearRect(0, 0, e.canvas.width, e.canvas.height), e.fillText(n, 0, 0), new Uint32Array(e.getImageData(0, 0, e.canvas.width, e.canvas.height).data));
            return t.every(function(e, t) {
                return e === r[t]
            })
        }
        function u(e, t, n) {
            switch (t) {
            case "flag":
                return n(e, "\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f", "\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f") ? !1 : !n(e, "\ud83c\uddfa\ud83c\uddf3", "\ud83c\uddfa\u200b\ud83c\uddf3") && !n(e, "\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f", "\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");
            case "emoji":
                return !n(e, "\ud83e\udef1\ud83c\udffb\u200d\ud83e\udef2\ud83c\udfff", "\ud83e\udef1\ud83c\udffb\u200b\ud83e\udef2\ud83c\udfff")
            }
            return !1
        }
        function f(e, t, n) {
            var r = "undefined" != typeof WorkerGlobalScope && self instanceof WorkerGlobalScope ? new OffscreenCanvas(300, 150) : i.createElement("canvas"),
                a = r.getContext("2d", {
                    willReadFrequently: !0
                }),
                o = (a.textBaseline = "top", a.font = "600 32px Arial", {});
            return e.forEach(function(e) {
                o[e] = t(a, e, n)
            }), o
        }
        function t(e) {
            var t = i.createElement("script");
            t.src = e,
            t.defer = !0,
            i.head.appendChild(t)
        }
        "undefined" != typeof Promise && (o = "wpEmojiSettingsSupports", s = ["flag", "emoji"], n.supports = {
            everything: !0,
            everythingExceptFlag: !0
        }, e = new Promise(function(e) {
            i.addEventListener("DOMContentLoaded", e, {
                once: !0
            })
        }), new Promise(function(t) {
            var n = function() {
                try {
                    var e = JSON.parse(sessionStorage.getItem(o));
                    if ("object" == typeof e && "number" == typeof e.timestamp && (new Date).valueOf() < e.timestamp + 604800 && "object" == typeof e.supportTests)
                        return e.supportTests
                } catch (e) {}
                return null
            }();
            if (!n) {
                if ("undefined" != typeof Worker && "undefined" != typeof OffscreenCanvas && "undefined" != typeof URL && URL.createObjectURL && "undefined" != typeof Blob)
                    try {
                        var e = "postMessage(" + f.toString() + "(" + [JSON.stringify(s), u.toString(), p.toString()].join(",") + "));",
                            r = new Blob([e], {
                                type: "text/javascript"
                            }),
                            a = new Worker(URL.createObjectURL(r), {
                                name: "wpTestEmojiSupports"
                            });
                        return void (a.onmessage = function(e) {
                            c(n = e.data),
                            a.terminate(),
                            t(n)
                        })
                    } catch (e) {}
                c(n = f(s, u, p))
            }
            t(n)
        }).then(function(e) {
            for (var t in e)
                n.supports[t] = e[t],
                n.supports.everything = n.supports.everything && n.supports[t],
                "flag" !== t && (n.supports.everythingExceptFlag = n.supports.everythingExceptFlag && n.supports[t]);
            n.supports.everythingExceptFlag = n.supports.everythingExceptFlag && !n.supports.flag,
            n.DOMReady = !1,
            n.readyCallback = function() {
                n.DOMReady = !0
            }
        }).then(function() {
            return e
        }).then(function() {
            var e;
            n.supports.everything || (n.readyCallback(), (e = n.source || {}).concatemoji ? t(e.concatemoji) : e.wpemoji && e.twemoji && (t(e.twemoji), t(e.wpemoji)))
        }))
    }((window, document), window._wpemojiSettings);
    /* ]]> */
    </script>
    <style id='wp-emoji-styles-inline-css'>
    img.wp-smiley, img.emoji {
        display: inline !important;
        border: none !important;
        box-shadow: none !important;
        height: 1em !important;
        width: 1em !important;
        margin: 0 0.07em !important;
        vertical-align: -0.1em !important;
        background: none !important;
        padding: 0 !important;
    }
    </style>
    <link rel='stylesheet' id='all-css-2' href='https://www.bufale.net/_static/??-eJyNyzsKgDAQRdENGYcUCinEteQzyOgkhkxEsnttBO0sL+8dOLOi5PkIKOBFIJBUcLz7TTG5YksDqY2xj5T6+9DBW6wCEQNZZIyY6icy24ZFMS7Wt3/83t79oDlOejRmGLXW5gKH0kGx' type='text/css' media='all'/>
    <style id='wp-block-library-inline-css'>
    .has-text-align-justify {
        text-align: justify;
    }
    </style>
    <style id='classic-theme-styles-inline-css'>
    /*! This file is auto-generated */
    .wp-block-button__link {
        color: #fff;
        background-color: #32373c;
        border-radius: 9999px;
        box-shadow: none;
        text-decoration: none;
        padding: calc(.667em + 2px) calc(1.333em + 2px);
        font-size:1.125em
    }

    .wp-block-file__button {
        background: #32373c;
        color: #fff;
        text-decoration: none
    }
    </style>
    <style id='global-styles-inline-css'>
    body {
        --wp--preset--color--black: #000000;
        --wp--preset--color--cyan-bluish-gray: #abb8c3;
        --wp--preset--color--white: #ffffff;
        --wp--preset--color--pale-pink: #f78da7;
        --wp--preset--color--vivid-red: #cf2e2e;
        --wp--preset--color--luminous-vivid-orange: #ff6900;
        --wp--preset--color--luminous-vivid-amber: #fcb900;
        --wp--preset--color--light-green-cyan: #7bdcb5;
        --wp--preset--color--vivid-green-cyan: #00d084;
        --wp--preset--color--pale-cyan-blue: #8ed1fc;
        --wp--preset--color--vivid-cyan-blue: #0693e3;
        --wp--preset--color--vivid-purple: #9b51e0;
        --wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg, rgba(6, 147, 227, 1) 0%, rgb(155, 81, 224) 100%);
        --wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg, rgb(122, 220, 180) 0%, rgb(0, 208, 130) 100%);
        --wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg, rgba(252, 185, 0, 1) 0%, rgba(255, 105, 0, 1) 100%);
        --wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg, rgba(255, 105, 0, 1) 0%, rgb(207, 46, 46) 100%);
        --wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg, rgb(238, 238, 238) 0%, rgb(169, 184, 195) 100%);
        --wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg, rgb(74, 234, 220) 0%, rgb(151, 120, 209) 20%, rgb(207, 42, 186) 40%, rgb(238, 44, 130) 60%, rgb(251, 105, 98) 80%, rgb(254, 248, 76) 100%);
        --wp--preset--gradient--blush-light-purple: linear-gradient(135deg, rgb(255, 206, 236) 0%, rgb(152, 150, 240) 100%);
        --wp--preset--gradient--blush-bordeaux: linear-gradient(135deg, rgb(254, 205, 165) 0%, rgb(254, 45, 45) 50%, rgb(107, 0, 62) 100%);
        --wp--preset--gradient--luminous-dusk: linear-gradient(135deg, rgb(255, 203, 112) 0%, rgb(199, 81, 192) 50%, rgb(65, 88, 208) 100%);
        --wp--preset--gradient--pale-ocean: linear-gradient(135deg, rgb(255, 245, 203) 0%, rgb(182, 227, 212) 50%, rgb(51, 167, 181) 100%);
        --wp--preset--gradient--electric-grass: linear-gradient(135deg, rgb(202, 248, 128) 0%, rgb(113, 206, 126) 100%);
        --wp--preset--gradient--midnight: linear-gradient(135deg, rgb(2, 3, 129) 0%, rgb(40, 116, 252) 100%);
        --wp--preset--font-size--small: 13px;
        --wp--preset--font-size--medium: 20px;
        --wp--preset--font-size--large: 36px;
        --wp--preset--font-size--x-large: 42px;
        --wp--preset--spacing--20: 0.44rem;
        --wp--preset--spacing--30: 0.67rem;
        --wp--preset--spacing--40: 1rem;
        --wp--preset--spacing--50: 1.5rem;
        --wp--preset--spacing--60: 2.25rem;
        --wp--preset--spacing--70: 3.38rem;
        --wp--preset--spacing--80: 5.06rem;
        --wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);
        --wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);
        --wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);
        --wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);
        --wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);
    }

    :where(.is-layout-flex) {
        gap: 0.5em;
    }

    :where(.is-layout-grid) {
        gap: 0.5em;
    }

    body .is-layout-flow > .alignleft {
        float: left;
        margin-inline-start: 0;
        margin-inline-end: 2em;
    }

    body .is-layout-flow > .alignright {
        float: right;
        margin-inline-start: 2em;
        margin-inline-end: 0;
    }

    body .is-layout-flow > .aligncenter {
        margin-left: auto !important;
        margin-right: auto !important;
    }

    body .is-layout-constrained > .alignleft {
        float: left;
        margin-inline-start: 0;
        margin-inline-end: 2em;
    }

    body .is-layout-constrained > .alignright {
        float: right;
        margin-inline-start: 2em;
        margin-inline-end: 0;
    }

    body .is-layout-constrained > .aligncenter {
        margin-left: auto !important;
        margin-right: auto !important;
    }

    body .is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)) {
        max-width: var(--wp--style--global--content-size);
        margin-left: auto !important;
        margin-right: auto !important;
    }

    body .is-layout-constrained > .alignwide {
        max-width: var(--wp--style--global--wide-size);
    }

    body .is-layout-flex {
        display: flex;
    }

    body .is-layout-flex {
        flex-wrap: wrap;
        align-items: center;
    }

    body .is-layout-flex > * {
        margin: 0;
    }

    body .is-layout-grid {
        display: grid;
    }

    body .is-layout-grid > * {
        margin: 0;
    }

    :where(.wp-block-columns.is-layout-flex) {
        gap: 2em;
    }

    :where(.wp-block-columns.is-layout-grid) {
        gap: 2em;
    }

    :where(.wp-block-post-template.is-layout-flex) {
        gap: 1.25em;
    }

    :where(.wp-block-post-template.is-layout-grid) {
        gap: 1.25em;
    }

    .has-black-color {
        color: var(--wp--preset--color--black) !important;
    }

    .has-cyan-bluish-gray-color {
        color: var(--wp--preset--color--cyan-bluish-gray) !important;
    }

    .has-white-color {
        color: var(--wp--preset--color--white) !important;
    }

    .has-pale-pink-color {
        color: var(--wp--preset--color--pale-pink) !important;
    }

    .has-vivid-red-color {
        color: var(--wp--preset--color--vivid-red) !important;
    }

    .has-luminous-vivid-orange-color {
        color: var(--wp--preset--color--luminous-vivid-orange) !important;
    }

    .has-luminous-vivid-amber-color {
        color: var(--wp--preset--color--luminous-vivid-amber) !important;
    }

    .has-light-green-cyan-color {
        color: var(--wp--preset--color--light-green-cyan) !important;
    }

    .has-vivid-green-cyan-color {
        color: var(--wp--preset--color--vivid-green-cyan) !important;
    }

    .has-pale-cyan-blue-color {
        color: var(--wp--preset--color--pale-cyan-blue) !important;
    }

    .has-vivid-cyan-blue-color {
        color: var(--wp--preset--color--vivid-cyan-blue) !important;
    }

    .has-vivid-purple-color {
        color: var(--wp--preset--color--vivid-purple) !important;
    }

    .has-black-background-color {
        background-color: var(--wp--preset--color--black) !important;
    }

    .has-cyan-bluish-gray-background-color {
        background-color: var(--wp--preset--color--cyan-bluish-gray) !important;
    }

    .has-white-background-color {
        background-color: var(--wp--preset--color--white) !important;
    }

    .has-pale-pink-background-color {
        background-color: var(--wp--preset--color--pale-pink) !important;
    }

    .has-vivid-red-background-color {
        background-color: var(--wp--preset--color--vivid-red) !important;
    }

    .has-luminous-vivid-orange-background-color {
        background-color: var(--wp--preset--color--luminous-vivid-orange) !important;
    }

    .has-luminous-vivid-amber-background-color {
        background-color: var(--wp--preset--color--luminous-vivid-amber) !important;
    }

    .has-light-green-cyan-background-color {
        background-color: var(--wp--preset--color--light-green-cyan) !important;
    }

    .has-vivid-green-cyan-background-color {
        background-color: var(--wp--preset--color--vivid-green-cyan) !important;
    }

    .has-pale-cyan-blue-background-color {
        background-color: var(--wp--preset--color--pale-cyan-blue) !important;
    }

    .has-vivid-cyan-blue-background-color {
        background-color: var(--wp--preset--color--vivid-cyan-blue) !important;
    }

    .has-vivid-purple-background-color {
        background-color: var(--wp--preset--color--vivid-purple) !important;
    }

    .has-black-border-color {
        border-color: var(--wp--preset--color--black) !important;
    }

    .has-cyan-bluish-gray-border-color {
        border-color: var(--wp--preset--color--cyan-bluish-gray) !important;
    }

    .has-white-border-color {
        border-color: var(--wp--preset--color--white) !important;
    }

    .has-pale-pink-border-color {
        border-color: var(--wp--preset--color--pale-pink) !important;
    }

    .has-vivid-red-border-color {
        border-color: var(--wp--preset--color--vivid-red) !important;
    }

    .has-luminous-vivid-orange-border-color {
        border-color: var(--wp--preset--color--luminous-vivid-orange) !important;
    }

    .has-luminous-vivid-amber-border-color {
        border-color: var(--wp--preset--color--luminous-vivid-amber) !important;
    }

    .has-light-green-cyan-border-color {
        border-color: var(--wp--preset--color--light-green-cyan) !important;
    }

    .has-vivid-green-cyan-border-color {
        border-color: var(--wp--preset--color--vivid-green-cyan) !important;
    }

    .has-pale-cyan-blue-border-color {
        border-color: var(--wp--preset--color--pale-cyan-blue) !important;
    }

    .has-vivid-cyan-blue-border-color {
        border-color: var(--wp--preset--color--vivid-cyan-blue) !important;
    }

    .has-vivid-purple-border-color {
        border-color: var(--wp--preset--color--vivid-purple) !important;
    }

    .has-vivid-cyan-blue-to-vivid-purple-gradient-background {
        background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;
    }

    .has-light-green-cyan-to-vivid-green-cyan-gradient-background {
        background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;
    }

    .has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background {
        background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;
    }

    .has-luminous-vivid-orange-to-vivid-red-gradient-background {
        background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;
    }

    .has-very-light-gray-to-cyan-bluish-gray-gradient-background {
        background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;
    }

    .has-cool-to-warm-spectrum-gradient-background {
        background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;
    }

    .has-blush-light-purple-gradient-background {
        background: var(--wp--preset--gradient--blush-light-purple) !important;
    }

    .has-blush-bordeaux-gradient-background {
        background: var(--wp--preset--gradient--blush-bordeaux) !important;
    }

    .has-luminous-dusk-gradient-background {
        background: var(--wp--preset--gradient--luminous-dusk) !important;
    }

    .has-pale-ocean-gradient-background {
        background: var(--wp--preset--gradient--pale-ocean) !important;
    }

    .has-electric-grass-gradient-background {
        background: var(--wp--preset--gradient--electric-grass) !important;
    }

    .has-midnight-gradient-background {
        background: var(--wp--preset--gradient--midnight) !important;
    }

    .has-small-font-size {
        font-size: var(--wp--preset--font-size--small) !important;
    }

    .has-medium-font-size {
        font-size: var(--wp--preset--font-size--medium) !important;
    }

    .has-large-font-size {
        font-size: var(--wp--preset--font-size--large) !important;
    }

    .has-x-large-font-size {
        font-size: var(--wp--preset--font-size--x-large) !important;
    }

    .wp-block-navigation a:where(:not(.wp-element-button)) {
        color: inherit;
    }

    :where(.wp-block-post-template.is-layout-flex) {
        gap: 1.25em;
    }

    :where(.wp-block-post-template.is-layout-grid) {
        gap: 1.25em;
    }

    :where(.wp-block-columns.is-layout-flex) {
        gap: 2em;
    }

    :where(.wp-block-columns.is-layout-grid) {
        gap: 2em;
    }

    .wp-block-pullquote {
        font-size: 1.5em;
        line-height: 1.6;
    }
    </style>
    <link rel='stylesheet' id='all-css-6' href='https://www.bufale.net/_static/??/wp-content/themes/bufale/style.css,/wp-content/mu-plugins/jetpack/css/jetpack.css?m=1699388732' type='text/css' media='all'/>
    <script type="text/javascript" src="https://www.bufale.net/_static/??-eJzTLy/QzcxLzilNSS3WzwKiwtLUokoopZebmaeXVayjj0+Rbm5melFiSSpUsX2uraGZpaWpmaGhoWUWAK++Iig="></script>
    <link rel="https://api.w.org/" href="https://www.bufale.net/wp-json/"/>
    <link rel="alternate" type="application/json" href="https://www.bufale.net/wp-json/wp/v2/pages/19162"/>
    <link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.bufale.net/xmlrpc.php?rsd"/>
    <meta name="generator" content="WordPress 6.4.1"/>
    <link rel='shortlink' href='https://www.bufale.net/?p=19162'/>
    <link rel="alternate" type="application/json+oembed" href="https://www.bufale.net/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.bufale.net%2Fthe-black-list-la-lista-nera-del-web%2F"/>
    <link rel="alternate" type="text/xml+oembed" href="https://www.bufale.net/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.bufale.net%2Fthe-black-list-la-lista-nera-del-web%2F&#038;format=xml"/>
    <script>
    var digistream_data = {
        "info_playlist_endpoint": "https:\/\/www.bufale.net\/wp-json\/digistream\/get_playlist_info",
        "wonder_marketing_url": "https:\/\/app.digitrend.it\/wonder-marketing",
        "digistream_url": "https:\/\/www.bufale.net\/wp-content\/plugins\/digistream\/",
        "site_url": "https:\/\/www.bufale.net",
        "digistream_version": "1.3.3",
        "digistream_playlist_js_date": 1685603091,
        "digistream_playlist_css_date": 1681222606,
        "altezza_header_mobile": 0,
        "colore_barra_descrizione": "#d0021b",
        "timer_tasto_chiusura_ad_lineari": 40,
        "timer_tasto_chiusura_ad_non_lineari": 15,
        "script_generali": ["https:\/\/app.digitrend.it\/wonder-marketing\/assets\/wordpress\/js\/digistream-players-manager.js?v=1685544503"]
    };
    </script>
    <style>
    @media (max-width: 575px) {
        .content_video.sticky {
            top: 0px !important;
        }

        .italpress-video-close {
            transform: translate(0, 0px) !important;
        }

        .init-playlist.sticky .dgt-mrk-digistream-playlist {
            top: 0px !important;
        }
    }

    .dgt-iframe-cont {
        width: 100%;
        max-width: 100% !important;
        padding-bottom: 56.25%;
        position: relative;
    }

    .dgt-iframe-cont > div > iframe, .dgt-iframe-cont > iframe, .dgt-iframe-cont > .fb-video {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
    }
    </style>
    <style>
    img#wpstats {
        display: none
    }
    </style>

    <!-- Google Tag Manager for WordPress by gtm4wp.com -->
    <!-- GTM Container placement set to off -->
    <script data-cfasync="false" data-pagespeed-no-defer>
    var dataLayer_content = {
        "pagePostType": "page",
        "pagePostType2": "single-page",
        "pagePostAuthor": "David Tyto Puente"
    };
    dataLayer.push(dataLayer_content);
    </script>
    <script type="text/javascript">
    console.warn && console.warn("[GTM4WP] Google Tag Manager container code placement set to OFF !!!");
    console.warn && console.warn("[GTM4WP] Data layer codes are active but GTM container must be loaded using custom coding !!!");
    </script>
    <!-- End Google Tag Manager for WordPress by gtm4wp.com -->

    <script type="application/ld+json" class="saswp-schema-markup-output">
    [{
        "@context": "https://schema.org",
        "@graph": [{
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Bufala",
            "url": "https://www.bufale.net/bufala/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Acchiappaclick",
            "url": "https://www.bufale.net/acchiappaclick-2/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Acchiappautenti",
            "url": "https://www.bufale.net/acchiappautenti/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Notizia Vera",
            "url": "https://www.bufale.net/notizia_vera/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Precisazioni",
            "url": "https://www.bufale.net/precisazioni/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Disinformazione",
            "url": "https://www.bufale.net/disinformazione/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Allarmismo",
            "url": "https://www.bufale.net/allarmismi/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Facebook",
            "url": "https://www.bufale.net/bufale-su-facebook/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Truffe",
            "url": "https://www.bufale.net/truffa/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "The Black List",
            "url": "https://www.bufale.net/the-black-list-la-lista-nera-del-web/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Guide Utili",
            "url": "https://www.bufale.net/guide-utili/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Chi Siamo",
            "url": "https://www.bufale.net/chi-siamo/"
        }, {
            "@context": "https://schema.org",
            "@type": "SiteNavigationElement",
            "@id": "https://www.bufale.net/#Principale",
            "name": "Fact Checking",
            "url": "https://www.bufale.net/fact-checking/"
        }]
    },

    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "@id": "https://www.bufale.net/the-black-list-la-lista-nera-del-web/#breadcrumb",
        "itemListElement": [{
            "@type": "ListItem",
            "position": 1,
            "item": {
                "@id": "https://www.bufale.net",
                "name": "Bufale"
            }
        }, {
            "@type": "ListItem",
            "position": 2,
            "item": {
                "@id": "https://www.bufale.net/the-black-list-la-lista-nera-del-web/",
                "name": "The Black List: la lista nera del web"
            }
        }]
    }]
    </script>

    <link rel="icon" href="https://www.bufale.net/wp-content/uploads/sites/5/2022/11/cropped-favicon.png?w=32" sizes="32x32"/>
    <link rel="icon" href="https://www.bufale.net/wp-content/uploads/sites/5/2022/11/cropped-favicon.png?w=192" sizes="192x192"/>
    <link rel="apple-touch-icon" href="https://www.bufale.net/wp-content/uploads/sites/5/2022/11/cropped-favicon.png?w=180"/>
    <meta name="msapplication-TileImage" content="https://www.bufale.net/wp-content/uploads/sites/5/2022/11/cropped-favicon.png?w=270"/>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700;800&family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
</head>
<body>
    <div id="div-gpt-ad-bufale-dsk_1x1"></div>

    <div id="search" class="">
        <span class="closebtn" title="Close Overlay">×</span>

        <div class="search-content">
            <form name="search_form" action="/" method="get" class="search_form">
                <input type="text" placeholder="Cerca" name="s">
                <button type="submit">
                    <i class="fa fa-search"></i>
                </button>
            </form>
        </div>
    </div>

    <header>
        <div class="navbar">

            <div class="logo-sito">
                <a href="https://www.bufale.net" title="Bufale">
                    <img class="img-responsive" src="https://www.bufale.net/wp-content/themes/bufale/images/logo_bufale.png">
                </a>
            </div>

            <div class="menu">

                <div class="social-mobile col-xs-12">
                    <ul>

                        <li>
                            <a class="social-icon" href="https://www.facebook.com/bufala/" title="Facebook" target="_blank">
                                <i class="fa fa-facebook"></i>
                            </a>
                            <h4>Facebook</h4>
                        </li>

                        <li>
                            <a class="social-icon" href="https://twitter.com/Bufalenet" title="Twitter" target="_blank">
                                <i class="fa fa-twitter"></i>
                            </a>
                            <h4>Twitter</h4>
                        </li>

                        <li>
                            <a class="social-icon" href="https://www.instagram.com/bufalenet/" title="Instagram" target="_blank">
                                <i class="fa fa-instagram"></i>
                            </a>
                            <h4>Instagram</h4>
                        </li>

                        <li>
                            <a class="social-icon" href="https://api.whatsapp.com/send?phone=393518501148" title="WhatsApp" target="_blank">
                                <i class="fa fa-whatsapp"></i>
                            </a>
                            <h4>WhatsApp</h4>
                        </li>

                        <li>
                            <a class="social-icon" href="https://t.me/bufale_fakenews" title="Telegram" target="_blank">
                                <i class="fa fa-telegram"></i>
                            </a>
                            <h4>Telegram</h4>
                        </li>
                    </ul>
                </div>
                <div class="menu-principale-container">
                    <ul id="menu-principale" class="">
                        <li id="menu-item-178962" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-178962">
                            <a href="https://www.bufale.net/bufala/">Bufala</a>
                            <ul class="sub-menu">
                                <li id="menu-item-178963" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-178963">
                                    <a href="https://www.bufale.net/acchiappaclick-2/">Acchiappaclick</a>
                                </li>
                                <li id="menu-item-178964" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-178964">
                                    <a href="https://www.bufale.net/acchiappautenti/">Acchiappautenti</a>
                                </li>
                            </ul>
                        </li>
                        <li id="menu-item-178965" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-178965">
                            <a href="https://www.bufale.net/notizia_vera/">Notizia Vera</a>
                            <ul class="sub-menu">
                                <li id="menu-item-178966" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-178966">
                                    <a href="https://www.bufale.net/precisazioni/">Precisazioni</a>
                                </li>
                            </ul>
                        </li>
                        <li id="menu-item-178967" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-178967">
                            <a href="https://www.bufale.net/disinformazione/">Disinformazione</a>
                            <ul class="sub-menu">
                                <li id="menu-item-178968" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-178968">
                                    <a href="https://www.bufale.net/allarmismi/">Allarmismo</a>
                                </li>
                            </ul>
                        </li>
                        <li id="menu-item-178969" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-178969">
                            <a href="https://www.bufale.net/bufale-su-facebook/">Facebook</a>
                        </li>
                        <li id="menu-item-178970" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-178970">
                            <a href="https://www.bufale.net/truffa/">Truffe</a>
                        </li>
                        <li id="menu-item-178971" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-178971">
                            <a href="https://www.bufale.net/the-black-list-la-lista-nera-del-web/">The Black List</a>
                        </li>
                        <li id="menu-item-178972" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-178972">
                            <a href="https://www.bufale.net/guide-utili/">Guide Utili</a>
                        </li>
                        <li id="menu-item-178973" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-178973">
                            <a href="https://www.bufale.net/chi-siamo/">Chi Siamo</a>
                        </li>
                        <li id="menu-item-222354" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-222354">
                            <a href="https://www.bufale.net/fact-checking/">Fact Checking</a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="social-bar">

                <div class="search" id="search-button">
                    <a class="btn-search-fullwidth openBtn">
                        <i class="fa fa-search"></i>
                    </a>
                </div>

                <ul class="nav navbar-nav navbar-right" style="width:100px">

                    <li>
                        <a class="social-icon hidden-xs hidden-sm" href="https://www.bufale.net/home/feed/" title="Feed" target="_blank">
                            <i class="fa fa-rss"></i>
                        </a>
                    </li>
                    <a class="social-icon hidden-xs hidden-sm" href="https://www.bufale.net/home/feed/" title="Feed" target="_blank"></a>
                    <li>
                        <a class="social-icon hidden-xs hidden-sm" href="https://www.bufale.net/home/feed/" title="Feed" target="_blank"></a>
                        <a class="social-icon hidden-xs hidden-sm" href="https://www.instagram.com/bufale_net" title="Instagram" target="_blank">
                            <i class="fa fa-instagram"></i>
                        </a>
                    </li>
                    <li>
                        <a class="social-icon hidden-xs hidden-sm" href="https://www.facebook.com/bufala" title="Facebook" target="_blank">
                            <i class="fa fa-facebook"></i>
                        </a>
                    </li>
                    <li>
                        <a class="social-icon hidden-xs hidden-sm" href="https://twitter.com/Bufalenet" title="Twitter" target="_blank">
                            <i class="fa fa-twitter"></i>
                        </a>
                    </li>

                </ul>

            </div>

            <div class="button-mobile-menu btn-mobile">
                <div class="bar1"></div>
                <div class="bar2"></div>
                <div class="bar3"></div>
            </div>

        </div>

    </header>
    <div class="container">
        <div class="left-column col-md-8">
            <div class="post-body">
                <div class="page-content">
                    <p style="text-align: justify">
                        <img fetchpriority="high" decoding="async" class="aligncenter wp-image-19250 " src="https://www.bufale.net/wp-content/uploads/sites/5/2016/01/blacklist-banner-300x158.jpg" alt="" width="402" height="212"/>
                    </p>
                    <p style="text-align: justify">Come promesso, in aggiornamento Black List e add-on. I siti che per più di un anno non abbiano pubblicato bufale o fatto disinformazione potranno essere rimossi come forma di incentivo positivo e critico, mentre le finte testate giornalistiche rimarranno dentro. Aspettiamo come sempre un vostro riscontro in merito, per poter di conseguenza migliorare il nostro servizio.</p>
                    <h3 style="text-align: justify">
                        <strong>False testate giornalistiche &#8220;satiriche&#8221;</strong>
                    </h3>
                    <p style="text-align: justify">Alcune esistono da diverso tempo, ma nel 2015 c&#8217;è stato un considerevole aumento delle &#8220;false testate giornalistiche&#8221;, o meglio di quei domini che hanno tratto in inganno molti utenti per via del loro nome facilmente confondibile con le più famose testate giornalistiche. Molte di queste si ritengono &#8220;satiriche&#8221; anche se, in alcuni casi, non hanno nulla a che vedere con la &#8220;satira&#8221;. Molti di questi siti, tuttavia, non sono più aggiornati da tempo, a causa del fatto che oggi, la maggior parte degli utenti ha imparato a riconoscere le &#8220;false testate giornalistiche&#8221;.</p>
                    <ul>
                        <li>
                            <a href="http://notiziepericolose.blogspot.it/">Dangerous News</a>
                        </li>
                        <li>
                            <a href="http://www.ilmattoquotidiano.it/">Il Matto Quotidiano</a>
                        </li>
                        <li>
                            <a href="http://www.ilmessaggio.it/">Ilmessaggio.it</a>
                        </li>
                        <li>
                            <a href="http://www.ilfattoquotidaino.it/" target="_blank" rel="noopener noreferrer">Il Fatto Quotidaino</a>
                        </li>
                        <li>
                            <a href="https://ilquotidaino.wordpress.com/" target="_blank" rel="noopener noreferrer">Il Quotidaino</a>
                        </li>
                        <li>
                            <a href="http://www.liberogiornale.com/" target="_blank" rel="noopener noreferrer">Libero Giornale</a>
                             (attenzione: ora è scritto in lingua indonesiana)
                        </li>
                        <li>
                            <a href="https://notiziariosegreto.wordpress.com" target="_blank" rel="noopener noreferrer">Notiziario Segreto</a>
                        </li>
                        <li>
                            <a href="http://secretnews.fr">Secret News</a>
                        </li>
                        <li>
                            <a href="http://superbamente.com">Superbamente</a>
                        </li>
                        <li>
                            <a href="http://worldnewsdailyreport.com">World News Daily Report</a>
                        </li>
                        <li>
                            <a href="https://www.fonteverificata.it">Fonte Verificata</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>Siti di bufale e disinformazione medica e scientifica</strong>
                    </h3>
                    <ul>
                        <li>
                            <a href="http://www.dionidream.com">Dionidream</a>
                        </li>
                        <li>
                            <a href="http://lastella.altervista.org/">La Stella</a>
                        </li>
                        <li>
                            <a href="http://www.segnidalcielo.it/">Segni dal cielo</a>
                        </li>
                        <li>
                            <a href="https://pianetablunews.wordpress.com/">Pianeta Blu News</a>
                        </li>
                        <li>
                            <a href="http://saltoquantico.org/">Salto Quantico</a>
                        </li>
                        <li>
                            <a href="https://autismovaccini.org/">Autismo e Vaccini</a>
                        </li>
                        <li>
                            <a href="http://www.jedanews.it/blog/">Jeda News</a>
                        </li>
                        <li>
                            <a href="https://www.naturalnews.com">Natural News</a>
                        </li>
                        <li>
                            <a href="http://www.notiziespericolate.com/" target="_blank" rel="noopener noreferrer">Notizie Spericolate</a>
                        </li>
                        <li>
                            <a href="https://viaggialowcost.altervista.org">Viaggia Low Cost</a>
                        </li>
                        <li>
                            <a href="https://sadefenza.blogspot.com">Sa Defenza</a>
                        </li>
                        <li>
                            <a href="https://www.renovatio21.com">Renovatio21</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>Siti di disinformazione politica</strong>
                    </h3>
                    <ul>
                        <li>
                            <a href="http://devinformarti.blogspot.it/?m=1">Devinformarti</a>
                        </li>
                        <li>
                            <a href="http://www.imolaoggi.it/">ImolaOggi</a>
                        </li>
                        <li>
                            <a href="https://scenarieconomici.it/">Scenari Economici</a>
                        </li>
                        <li>
                            <a href="https://voxnews.info/">Voxnews</a>
                        </li>
                        <li>
                            <a href="http://www.informarexresistere.fr/">Informare X Resistere</a>
                        </li>
                        <li>
                            <a href="http://www.jedanews.it/blog/" target="_blank" rel="noopener noreferrer">Jeda News</a>
                        </li>
                        <li>
                            <a href="http://www.breaknotizie.com/" target="_blank" rel="noopener noreferrer">BreakNotizie</a>
                        </li>
                        <li>
                            <a href="http://www.direttanews24.com/" target="_blank" rel="noopener noreferrer">DirettaNews24</a>
                        </li>
                        <li>
                            <a href="http://www.fascinazione.info/" target="_blank" rel="noopener noreferrer">FascinAzione</a>
                        </li>
                        <li>
                            <a href="http://www.notiziespericolate.com/">Notizie Spericolate</a>
                        </li>
                        <li>
                            <a href="http://tg5stelle.it/" target="_blank" rel="noopener noreferrer">TG5Stelle</a>
                        </li>
                        <li>
                            <a href="http://blogopenyoureyes.altervista.org/" target="_blank" rel="noopener noreferrer">Open Your Eyes</a>
                        </li>
                        <li>
                            <a href="http://ilbazarinformazione.blogspot.it/" target="_blank" rel="noopener noreferrer">Il Bazaar Informazione</a>
                        </li>
                        <li>
                            <a href="http://informare.over-blog.it/" target="_blank" rel="noopener noreferrer">Informare</a>
                        </li>
                        <li>
                            <a href="http://notizieinmovimentonews.blogspot.it/" target="_blank" rel="noopener noreferrer">Notizie in Movimento</a>
                        </li>
                        <li>
                            <a href="https://www.tg24-ore.com">Notizie 24 Ore</a>
                        </li>
                        <li>
                            <a href="https://sadefenza.blogspot.com">Sa Defenza</a>
                        </li>
                        <li>
                            <a href="https://informaresenzacensure.blogspot.com">Informare Senza Censure</a>
                        </li>
                        <li>
                            <a href="http://www.byoblu.com">ByoBlu</a>
                        </li>
                        <li>
                            <a href="https://www.mag24.es">Mag24</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>Siti di disinformazione a sfondo religioso e/o razziale</strong>
                    </h3>
                    <ul>
                        <li>
                            <a href="https://voxnews.info/" target="_blank" rel="noopener noreferrer">Voxnews</a>
                        </li>
                        <li>
                            <a href="http://www.imolaoggi.it/">ImolaOggi</a>
                        </li>
                        <li>
                            <a href="http://ilbazarinformazione.blogspot.it/" target="_blank" rel="noopener noreferrer">Il Bazaar Informazione</a>
                        </li>
                        <li>
                            <a href="https://www.tg24-ore.com">Notizie 24 Ore</a>
                        </li>
                        <li>
                            <a href="https://sadefenza.blogspot.com">Sa Defenza</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>Siti di bufale scandalistiche</strong>
                    </h3>
                    <ul style="text-align: justify">
                        <li>
                            <a href="http://devinformarti.blogspot.it/?m=1">Devinformarti</a>
                        </li>
                        <li>
                            <a href="http://www.iocritico.com/">Io critico</a>
                        </li>
                        <li>
                            <a href="https://scenarieconomici.it/">Scenari Economici</a>
                        </li>
                        <li>
                            <a href="http://www.sostenitori.info/" target="_blank" rel="noopener noreferrer">Sostenitori delle Forze dell&#8217;Ordine</a>
                        </li>
                        <li>
                            <a href="http://irresponsabile.com/" target="_blank" rel="noopener noreferrer">L&#8217;irresponsabile</a>
                        </li>
                        <li>
                            <a href="http://www.notiziespericolate.com/">Notizie Spericolate</a>
                        </li>
                        <li>
                            <a href="http://aidaa-animaliambiente.blogspot.it/" target="_blank" rel="noopener noreferrer">AnimaliAmbiente</a>
                        </li>
                        <li>
                            <a href="http://ilbazarinformazione.blogspot.it/" target="_blank" rel="noopener noreferrer">Il Bazaar Informazione</a>
                        </li>
                        <li>
                            <a href="http://thuglifevideos.com">Thug Life Videos</a>
                        </li>
                        <li>
                            <a href="http://yournewswire.com">Your News Wire</a>
                        </li>
                        <li>
                            <a href="https://www.tg24-ore.com">Notizie 24 Ore</a>
                        </li>
                        <li>
                            <a href="https://viaggialowcost.altervista.org">Viaggia Low Cost</a>
                        </li>
                        <li>
                            <a href="https://sadefenza.blogspot.com">Sa Defenza</a>
                        </li>
                        <li>
                            <a href="https://www.maurizioblondet.it">Maurizio Blondet</a>
                        </li>
                        <li>
                            <a href="https://informaresenzacensure.blogspot.com">Informare Senza Censure</a>
                        </li>
                        <li>
                            <a href="https://www.mag24.es">Mag24</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>Siti di bufale a sfondo politico e razziale</strong>
                    </h3>
                    <ul>
                        <li>
                            <a href="http://www.sostenitori.info/" target="_blank" rel="noopener noreferrer">Sostenitori delle Forze dell&#8217;Ordine</a>
                        </li>
                        <li>
                            <a href="http://devinformarti.blogspot.it/?m=1">Devinformarti</a>
                        </li>
                        <li>
                            <a href="http://www.direttanews24.com/" target="_blank" rel="noopener noreferrer">DirettaNews2</a>
                            <a href="http://www.direttanews24.com/">4</a>
                        </li>
                        <li>
                            <a href="http://www.fascinazione.info/" target="_blank" rel="noopener noreferrer">FascinAzione</a>
                        </li>
                        <li>
                            <a href="http://ilbazarinformazione.blogspot.it/" target="_blank" rel="noopener noreferrer">Il Bazaar Informazione</a>
                        </li>
                        <li>
                            <a href="https://www.tg24-ore.com">Notizie 24 Ore</a>
                        </li>
                        <li>
                            <a href="https://sadefenza.blogspot.com">Sa Defenza</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>Siti clickbait</strong>
                    </h3>
                    <p style="text-align: justify">
                        <em>Aggregatori di notizie, copia incollatori, senza alcuna verifica dei fatti e titoli accattivanti per attrarre il lettore.</em>
                    </p>
                    <ul>
                        <li>
                            <a href="http://www.dionidream.com">Dionidream</a>
                        </li>
                        <li>
                            <a href="http://www.essere-informati.it/">Essere Informati</a>
                        </li>
                        <li>
                            <a href="http://www.tgnewsitalia.it/wp/">TGNewsItalia</a>
                        </li>
                        <li>
                            <a href="http://voxnews.info/">Voxnews</a>
                        </li>
                        <li>
                            <a href="http://www.nocensura.com/">NoCensura</a>
                        </li>
                        <li>
                            <a href="http://tuttiicriminidegliimmigrati.com/">Tuttiicriminidegliimmigrati</a>
                        </li>
                        <li>
                            <a href="http://www.vnews24.it/">VNews24</a>
                        </li>
                        <li>
                            <a href="http://www.tgnewsitalia.it/wp/">TGNewsItalia</a>
                        </li>
                        <li>
                            <a href="http://www.direttanews.it/" target="_blank" rel="noopener noreferrer">
                                DirettaNews
                                <br/>
                            </a>
                        </li>
                        <li>
                            <a href="http://www.direttanews24.com/" target="_blank" rel="noopener noreferrer">DirettaNews24</a>
                        </li>
                        <li>
                            <a href="http://informatitalia.blogspot.it/">Informati, Italia</a>
                        </li>
                        <li>
                            <a href="http://www.internapoli.it">InterNapoli</a>
                        </li>
                        <li>
                            <a href="http://www.jedanews.it/blog/" target="_blank" rel="noopener noreferrer">Jeda News</a>
                        </li>
                        <li>
                            <a href="http://newscronaca.it/" target="_blank" rel="noopener noreferrer">News Cronaca</a>
                        </li>
                        <li>
                            <a href="http://www.notiziespericolate.com/">Notizie Spericolate</a>
                        </li>
                        <li>
                            <a href="http://www.perdavvero.com/" target="_blank" rel="noopener noreferrer">Per Davvero</a>
                        </li>
                        <li>
                            <a href="http://socialbuzz.it/" target="_blank" rel="noopener noreferrer">SocialBuzz</a>
                        </li>
                        <li>
                            <a href="http://tg5stelle.it/" target="_blank" rel="noopener noreferrer">TG5Stelle</a>
                        </li>
                        <li>
                            <a href="http://thuglifevideos.com">Thug Life Videos</a>
                        </li>
                        <li>
                            <a href="http://direttanfo.blogspot.it/" target="_blank" rel="noopener noreferrer">DirettaNfo</a>
                        </li>
                        <li>
                            <a href="https://www.tg24-ore.com">TG24-ore</a>
                        </li>
                        <li>
                            <a href="https://viaggialowcost.altervista.org">Viaggia Low Cost</a>
                        </li>
                        <li>
                            <a href="https://sadefenza.blogspot.com">Sa Defenza</a>
                        </li>
                        <li>
                            <a href="https://www.maurizioblondet.it">Maurizio Blondet</a>
                        </li>
                        <li>
                            <a href="https://informaresenzacensure.blogspot.com">Informare Senza Censure</a>
                        </li>
                        <li>
                            <a href="http://www.byoblu.com">ByoBlu</a>
                        </li>
                        <li>
                            <a href="https://www.mag24.es">Mag24</a>
                        </li>
                        <li>
                            <a href="https://www.worldnotix.net">WorldNotix</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>Pagine social clickbait</strong>
                    </h3>
                    <p style="text-align: justify">
                        <em>Aggregatori di notizie, molto spesso queste pagine sono satelliti dei siti clickbait. Riportano notizie frammentarie con titoli ad effetto per costringere i lettori a cliccare sui link in allegato</em>
                    </p>
                    <ul>
                        <li>
                            <a href="https://www.facebook.com/italiaagliitaliani1/?__cft__[0]=AZXnPO5ffX6kDpN6Ejp0Gw96bWLvyTHe0PDpLaPZJFvSJE_QxR_KWA4klYerjWKG-Mk8k2fbz-sy5sB3x38n0fzWx2ITLhSaAX5OJQgB_ZmyvcFCaZOqxyTx3_TmffEd9Qw5q_lhCKsc9_muhZznACw7vhi8z6FrSWiZYNUyL83CnoF6b8EflSD6osq7vDbmH7nzkpofRtcUbfMsISVMH4mLuDCe0EtuF8xr0zlwHfg2NQ&amp;__tn__=-UC*F">L&#8217;Italia agli italiani</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/enjoymimanchi">Mi Manchi</a>
                        </li>
                    </ul>
                    <h3>
                        <strong>I siti e le pagine social di complottisti e bufalari</strong>
                    </h3>
                    <p style="text-align: justify">
                        <em>Nuovo Ordine Mondiale, Scie chimiche, alieni, 11 settembre&#8230; chi più ne ha più ne metta.</em>
                    </p>
                    <ul>
                        <li>
                            <a href="http://sulatestagiannilannes.blogspot.it/">Su la testa – Gianni Lannes</a>
                        </li>
                        <li>
                            <a href="http://saltoquantico.org/">Salto Quantico</a>
                        </li>
                        <li>
                            <a href="https://scenarieconomici.it/">Scenari economici</a>
                        </li>
                        <li>
                            <a href="http://www.tmcrew.org/">Tactical Media Crew</a>
                        </li>
                        <li>
                            <a href="http://www.tanker-enemy.com/">Tanker Enemy</a>
                        </li>
                        <li>
                            <a href="http://www.tankerenemy.com/">Tanker Enemy Blog</a>
                        </li>
                        <li>
                            <a href="http://www.jedanews.it/blog/">Jeda News</a>
                        </li>
                        <li>
                            <a href="http://www.segnidalcielo.it/">Segni dal cielo</a>
                        </li>
                        <li>
                            <a href="http://www.nocensura.com/">NoCensura</a>
                        </li>
                        <li>
                            <a href="https://voxnews.info/">Voxnews</a>
                        </li>
                        <li>
                            <a href="http://sapereeundovere.com/">Sapere è un dovere</a>
                        </li>
                        <li>
                            <a href="http://www.informarexresistere.fr/">Informare X Resistere</a>
                        </li>
                        <li>
                            <a href="http://www.luogocomune.net/LC/">Luogocomune</a>
                        </li>
                        <li>
                            <a href="https://pianetablunews.wordpress.com/">Pianeta Blu News</a>
                        </li>
                        <li>
                            <a href="http://www.disinformazione.it">Disinformazione</a>
                        </li>
                        <li>
                            <a href="http://www.centrometeoitaliano.it/">Centro Meteo Italiano</a>
                        </li>
                        <li>
                            <a href="http://informatitalia.blogspot.it/">Informati, Italia</a>
                        </li>
                        <li>
                            <a href="http://www.notiziespericolate.com/" target="_blank" rel="noopener noreferrer">Notizie Spericolate</a>
                        </li>
                        <li>
                            <a href="http://www.signoraggio.it/" target="_blank" rel="noopener noreferrer">Signoraggio</a>
                        </li>
                        <li>
                            <a href="http://albainternazionale.blogspot.it/">Vincenzo Ferraro Blog</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/oggi24ore">Oggi 24 Ore</a>
                        </li>
                        <li>
                            <a href="https://sadefenza.blogspot.com">Sa Defenza</a>
                        </li>
                        <li>
                            <a href="https://www.maurizioblondet.it">Maurizio Blondet</a>
                        </li>
                        <li>
                            <a href="https://informaresenzacensure.blogspot.com">Informare Senza Censure</a>
                        </li>
                    </ul>
                    <p style="text-align: justify">Le pagine social:</p>
                    <ul>
                        <li>
                            <a href="https://www.facebook.com/Scienza-di-Confine-188189217954979/">Scienza di confine</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/StopInvasioneClandestina/">Stop Invasione</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/noncielodicono/">Non cielo dicono</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/RobyFanpage.It/?ref=br_rs">Roby</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/sardegnatoday/">Sardegna Today</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/oggi24ore">Oggi 24 Ore</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/sadefenza/">Sa Defenza</a>
                        </li>
                        <li>
                            <a href="https://twitter.com/RadioSavana?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor">Radio Savana</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/Quello-che-non-ci-dicono-107884204213182">Quello che non ci dicono</a>
                        </li>
                        <li>
                            <a href="https://www.facebook.com/websocialtv/">SocialTV Network</a>
                             (Facebook)
                        </li>
                        <li>
                            <a href="https://twitter.com/socialtvntw">SocialTV Network</a>
                             (Twitter)
                        </li>
                    </ul>
                    <h3>Personaggi pubblici</h3>
                    <p style="text-align: justify">
                        <em>Spesso considerati dei guru dell&#8217;informazione per la loro penna acuminata e per la loro capacità dialettica, ma per chi li segue abbiamo brutte notizie: nessuno è infallibile.</em>
                    </p>
                    <ul>
                        <li>
                            <em>in aggiornamento</em>
                        </li>
                    </ul>
                    <h3>
                        <strong>Testate giornalistiche</strong>
                    </h3>
                    <p style="text-align: justify">E le testate giornalistiche? Certo, abbiamo riportato numerosi casi in cui testate giornalistiche hanno pubblicato bufale, disinformazione o allarmismo. Di certo non è tecnicamente possibile porle allo stesso livello di altri siti qua sopra citati. Certo è che spesso gli articoli di queste testate giornalistiche vengono copiati, incollati e modificati dai siti di bufale e disinformazione per secondi fini.</p>
                    <p>
                        Siti satirici [
                        <span style="color: #ff0000">da non considerare come parte della lista nera</span>
                        ]
                    </p>
                    <p style="text-align: justify">
                        Questi siti sono fatti apposta per diffondere 
                        <strong>pillole di satira e qualche risata</strong>
                        . Succede spesso che alcuni utenti ce li segnalino pure&#8230; 
                        <span style="color: #ff0000">
                            <strong>Non sono da &#8220;lista nera&#8221;</strong>
                        </span>
                        , ma li riportiamo siccome a volte
                        <strong> le loro simpatiche &#8220;bufale&#8221; vengono copiate e incollate da parte dei siti elencati qua sopra</strong>
                        .
                    </p>
                    <ul>
                        <li>
                            <a href="http://www.lercio.it/">Lercio</a>
                        </li>
                        <li>
                            <a href="http://chiaveorgonica.altervista.org/">Chiave Orgonica</a>
                        </li>
                    </ul>
                    <p style="text-align: justify">
                        Ricordiamo il triste caso dell&#8217;articolo satirico dei rom ed il gattino di Lercio che Catena Umana sfruttò (
                        <a href="http://www.bufale.net/home/bufala-orrore-nel-campo-rom-gonfiano-un-gattino-col-compressore-muore-dopo-un-volo-di-15mt-bufale-net/">leggi articolo</a>
                        ).
                    </p>
                </div>
            </div>
        </div>

        <div class="sidebar col-md-4 hidden-xs hidden-sm">

            <div class="widget_element">
                <div class="medium-top">
                    <!-- friendly name: adk_spalla-top -->
                    <div class="adk-slot">
                        <div id="adk_spalla-top" style="min-height: 600px;" data-google-query-id="" class="hidden">
                            <div id="google_ads_iframe_/21625262017,38326652/Mosai.co/bufale.net/spalla-top_0__container__" style="border: 0pt none; width: 300px; height: 0px;"></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="widget_element">
                <div id="sidebar_bufala">
                    <div class="whatsapp">
                        <a href="https://api.whatsapp.com/send?phone=393518501148 ">
                            <img src="https://www.bufale.net/wp-content/themes/bufale/images/segnala_una_bufala.png" class="img-responsive">
                        </a>
                    </div>
                </div>
            </div>

            <div class="widget_element">
                <div id="sidebar_blacklist">
                    <div class="black-list">
                        <a href="https://www.bufale.net/home/the-black-list-la-lista-nera-del-web/">
                            <img src="https://www.bufale.net/wp-content/themes/bufale/images/black_list.png" class="img-responsive">
                        </a>
                    </div>

                </div>
            </div>

            <div class="widget_element">
                <div id="sidebar_fakenews">
                    <div class="red-widget">
                        <a href="https://chrome.google.com/webstore/detail/bufalenet/kjaemgaefcbfjbgglbomigclhhioggod?hl=it">
                            <img src="https://www.bufale.net/wp-content/themes/bufale/images/adblock.png" class="img-responsive">
                        </a>
                    </div>

                </div>
            </div>

            <div class="widget_element">
                <div id="sidebar_invia">
                    <div class="send-article">
                        <a href="https://www.bufale.net/home/diventa-uno-sbufalatore-stupisci-gli-amici-al-resto-pensiamo-scuola-debunking/">
                            <img src="https://www.bufale.net/wp-content/themes/bufale/images/INVIA_ARTICOLO.png" class="img-responsive">
                        </a>
                    </div>

                </div>
            </div>

            <div class="widget_element">
                <div class="banner skyscreaper-desktop">
                    <!-- friendly name: adk_spalla-middle -->
                    <div class="adk-slot">
                        <div id="adk_spalla-middle" style="min-height: 600px;" data-google-query-id="" class="hidden">
                            <div id="google_ads_iframe_/21625262017,38326652/Mosai.co/bufale.net/spalla-middle_0__container__" style="border: 0pt none; width: 300px; height: 0px;"></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="widget_element">
                <div id="best-articles">
                    <div class="best-articles">
                        <div class="title-best">
                            <h2>Articolo più letto</h2>
                        </div>

                        <div class="part-1">
                            <div class="img">
                                <a href="https://www.bufale.net/enrico-montesano-cielo-scie-croce/" title="Messaggio divino o scie chimiche? Il dubbio dei follower di Enrico Montesano">

                                    <div class="image-background-container" id="image_636e5f7e2912d" style="background-image: url(&quot;https://static.nexilia.it/bufale/2021/05/montesano-copertina-297x198.jpg&quot;);">

                                        <img src="https://www.bufale.net/wp-content/themes/bufale/images/sizes/best-articles.png?version=4.0" rel="nofollow" class="max-responsive">

                                        <script>
                                        lazyImg('image_636e5f7e2912d');
                                        </script>
                                    </div>

                                </a>
                            </div>

                            <div class="title">
                                <h2>
                                    <a href="https://www.bufale.net/enrico-montesano-cielo-scie-croce/"> Messaggio divino o scie chimiche? Il dubbio dei follower di Enrico...</a>
                                </h2>
                            </div>

                            <div class="author">
                                <h4>
                                    di 
                                    <a href="https://www.bufale.net/author/starlight/">Starlight</a>
                                </h4>
                            </div>

                        </div>

                    </div>

                    <div id="fb-root"></div>
                    <script class="_iub_cs_activate" type="text/plain">
                    (function(d, s, id) {
                        var js,
                            fjs = d.getElementsByTagName(s)[0];
                        if (d.getElementById(id))
                            return;
                        js = d.createElement(s);
                        js.id = id;
                        js.src = 'https://connect.facebook.net/it_IT/sdk.js#xfbml=1&version=v3.2&appId=337667276835378&autoLogAppEvents=1';
                        fjs.parentNode.insertBefore(js, fjs);
                    }(document, 'script', 'facebook-jssdk'));
                    </script>

                    <div class="fb-page" data-href="https://www.facebook.com/bufala" data-tabs="" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true">
                        <blockquote cite="https://www.facebook.com/bufala" class="fb-xfbml-parse-ignore">
                            <a href="https://www.facebook.com/bufala">Bufale</a>
                        </blockquote>
                    </div>
                </div>
            </div>

            <div class="widget_element">

                <div id="adv_medium_bottom-sticky-wrapper" class="sticky-wrapper" style="height: 0px;">
                    <div class="banner" id="adv_medium_bottom" style="width: 283.325px;">
                        <!-- friendly name: adk_spalla-bottom -->
                        <div class="adk-slot">
                            <div id="adk_spalla-bottom" style="min-height: 600px;" data-google-query-id="" class="hidden">
                                <div id="google_ads_iframe_/21625262017,38326652/Mosai.co/bufale.net/spalla-bottom_0__container__" style="border: 0pt none; width: 300px; height: 0px;"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                jQuery(document).ready(function() {
                    if (document.documentElement.clientWidth > 1000) {
                        loadScript("https://cdnjs.cloudflare.com/ajax/libs/jquery.sticky/1.0.4/jquery.sticky.min.js", function() {
                            jQuery("#adv_medium_bottom").sticky({
                                topSpacing: 30
                            });
                        });
                    }
                });
                </script>
            </div>
        </div>
    </div>
    <!-- Chiusura div container -->
    </div>

    <footer>
        <div class="part-1 hidden-xs">
            <div class="container" style="margin-top: 0">

                <div class="logo-footer col-md-6 col-sm-6">
                    <a href="https://www.bufale.net" title="Bufale">
                        <!-- INSERIRE LOGO SITO -->
                        <img class="img-responsive" src="https://www.bufale.net/wp-content/themes/bufale/images/logo_bufale.png">
                    </a>
                </div>

                <div class="description col-md-6 col-sm-6 hidden-xs">
                    <p>Bufale.net è un servizio contro le fake news a disposizione dei cittadini ideato, fondato e diretto
                                        da Claudio Michelizza e Fabio Milella.</p>

                    <p>
                        Se il nostro servizio ti piace sostienici su 
                        <a href="https://www.patreon.com/bufale" target="_blank">PATREON</a>
                         o
                                            con una donazione
                                            
                        <a href="https://www.paypal.me/bufalenet" target="_blank">PAYPAL</a>
                        .
                    </p>

                    <p> ©Copyright 2018, All Rights Reserved</p>
                </div>
            </div>
        </div>

        <div class="part-2">
            <div class="container" style="margin-top: 0; background-color: #d0021b">

                <div class="col-xs-4">
                    <div class="logo-digitrend">
                        <a href="https://digitrend.it/" target="_blank">
                            <img src="https://www.bufale.net/wp-content/themes/bufale/images/digitrend.png" class="img-responsive">
                        </a>
                    </div>
                </div>

                <div class="col-xs-8 no-pad">
                    <div class="menu-footer">
                        <ul id="menu-servizio" class="">
                            <li id="menu-item-178974" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-178974">
                                <a href="https://www.bufale.net/la-redazione/">La Redazione</a>
                            </li>
                            <li id="menu-item-178958" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-178958">
                                <a href="https://www.bufale.net/contatti/">Contatti</a>
                            </li>
                            <li id="menu-item-178959" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-178959">
                                <a href="https://www.bufale.net/dicono-di-noi/">Dicono di noi</a>
                            </li>
                            <li id="menu-item-197664" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-197664">
                                <a href="https://www.bufale.net/privacy-policy/">Privacy Policy</a>
                            </li>
                            <li id="menu-item-197665" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-197665">
                                <a href="https://www.bufale.net/cookie-policy/">Cookie Policy</a>
                            </li>
                            <li id="menu-item-197666" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-197666">
                                <a href="#" onclick="if(window.__lxG__consent__ !== undefined) {window.__lxG__consent__.showConsent()} else {alert('This function only for users from European Economic Area (EEA)')}; return false">Impostazioni Cookie</a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="description col-xs-6 hidden-sm hidden-md hidden-lg">
                    <p>Bufale.net è un servizio contro le fake news a disposizione dei cittadini ideato, fondato e diretto
                                        da Claudio Michelizza e Fabio Milella.</p>

                    <p>
                        Se il nostro servizio ti piace sostienici su 
                        <a href="https://www.patreon.com/bufale" target="_blank">PATREON</a>
                         o
                                            con una donazione
                                            
                        <a href="https://www.paypal.me/bufalenet" target="_blank">PAYPAL</a>
                        .
                    </p>

                    <p> ©Copyright 2018, All Rights Reserved</p>
                </div>
            </div>
        </div>
    </footer>
    <script defer type="text/javascript" src="https://stats.wp.com/e-202346.js" id="jetpack-stats-js"></script>
    <script type="text/javascript" id="jetpack-stats-js-after">
    /* <![CDATA[ */
    _stq = window._stq || [];
    _stq.push(["view", {
        v: 'ext',
        blog: '212329502',
        post: '19162',
        tz: '1',
        srv: 'www.bufale.net',
        hp: 'vip',
        j: '1:12.7.1'
    }]);
    _stq.push(["clickTrackerInit", "212329502", "19162"]);
    /* ]]> */
    </script>
    <script>
    (function($) {
        var w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        $(".fix-load").removeClass("fix-load");
        $(document).ready(function() {
            $(".menu-item-197666 > a").addClass("iubenda-advertising-preferences-link")
        });
        if (w < 992) {
            $(window).click(function() {
                $(".menu-item-has-children").removeClass("is-active")
            });
            $(".menu-item-has-children > a").on("click", function(evt) {
                if ($(".is-active")[0]) {
                    $(".menu-item-has-children").not($(this).parent()).removeClass("is-active");
                    $(this).parent().toggleClass("is-active")
                } else {
                    evt.preventDefault();
                    evt.stopPropagation();
                    $(".menu-item-has-children").not($(this).parent()).removeClass("is-active");
                    $(this).parent().toggleClass("is-active")
                }
            })
        }
        $(".button-mobile-menu").click(function() {
            $("body").toggleClass("open-menu");
            $(this).toggleClass("change")
        });
        $("#search-button").click(function() {
            $("#search").addClass("open")
        });
        $("#search .closebtn").click(function() {
            $("#search").removeClass("open")
        });
        if (typeof Swiper !== "undefined") {
            new Swiper("#swiper-bufale", {
                slidesPerView: 3,
                spaceBetween: 10,
                breakpoints: {
                    767: {
                        slidesPerView: "auto",
                        spaceBetween: 20
                    }
                },
                pagination: {
                    el: "#swiper-bufale .swiper-pagination",
                    clickable: true
                }
            })
        }
        switch (true) {
        case w < 768 && w > 374:
            $(".preview-single-archive-post .title h2 a").each(function() {
                $().createExcerpts($(this), 110, "...")
            });
            $(".preview-single-home-post .title h2 a").each(function() {
                $().createExcerpts($(this), 70, "...")
            });
            $(".title-main-post h2 a").each(function() {
                $().createExcerpts($(this), 80, "...")
            });
            $(".main-post-archive .title h2 a").each(function() {
                $().createExcerpts($(this), 85, "...")
            });
            $(".description-main-post p").each(function() {
                $().createExcerpts($(this), 150, "...")
            });
            break;
        case w < 375:
            $(".preview-single-archive-post .title h2 a").each(function() {
                $().createExcerpts($(this), 85, "...")
            });
            $(".preview-single-home-post .title h2 a").each(function() {
                $().createExcerpts($(this), 50, "...")
            });
            $(".title-main-post h2 a").each(function() {
                $().createExcerpts($(this), 50, "...")
            });
            $(".main-post-archive .title h2 a").each(function() {
                $().createExcerpts($(this), 80, "...")
            });
            $(".description-main-post p").each(function() {
                $().createExcerpts($(this), 200, "...")
            });
            $(".archive .single-archive-post .preview-single-archive-post .title h2 a").each(function() {
                $().createExcerpts($(this), 120, "...")
            });
            break;
        default:
            $(".preview-single-home-post .title h2 a").each(function() {
                $().createExcerpts($(this), 50, "...")
            });
            $(".preview-single-archive-post .title h2 a").each(function() {
                $().createExcerpts($(this), 80, "...")
            });
            $(".title-main-post h2 a").each(function() {
                $().createExcerpts($(this), 140, "...")
            });
            $(".main-post-archive .title h2 a").each(function() {
                $().createExcerpts($(this), 90, "...")
            });
            $(".main-post-archive .description p").each(function() {
                $().createExcerpts($(this), 200, "...")
            });
            $(".description-main-post p").each(function() {
                $().createExcerpts($(this), 120, "...")
            })
        }
    })(jQuery);
    </script>

    <!-- OneTagSour Website Inputs-->
    <script type="text/javascript">
    window._sour = {
        pageType: "home"
    }
    </script>
    <!-- End OneTagSour -->

    <!-- OneTagSour -->
    <script type="text/javascript" src="https://cdn.codesour.com/codesour/bufale.net/bufale.net.prod.js"></script>
    <!-- End OneTagSour -->

</body>
</html>
'''

#URL = "http://devinformarti.blogspot.it/?m=1"

#page = requests.get(URL)

soup = BeautifulSoup(text, "html.parser")
div = soup.find('div',class_='post-body')
lis=div.findAll('li')

domains={
    'www.facebook.com':0,
    'www.youtube.com':0,
    'www.twitter.com':0,
    'twitter.com':0,
    'www.instagram.com':0,
    't.me':0,
    'telegram.me':0,
    'vimeo.com':0
}
for li in lis:
    if li.find('a') is not None:
        url = li.find('a')['href']
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain in domains:
            continue
        domains[domain]=0
        print(domain+',butac.net'+',blacklist')

domains={
    'www.facebook.com':0,
    'www.youtube.com':0,
    'www.twitter.com':0,
    'twitter.com':0,
    'www.instagram.com':0,
    't.me':0,
    'telegram.me':0,
    'vimeo.com':0
}
jsontext=requests.get('https://raw.githubusercontent.com/flodd/butac_black_list/main/black_list.json').json()
for value in jsontext['items']:

    for url in value['items']:
        domain=urlparse(url['url']).netloc
        if domain in domains:
            continue
        domains[domain]=0
        #print(urlparse(url['url']).netloc)
        print(domain+',bufale.net'+',blacklist')

