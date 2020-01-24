// Copyright 2006-2018 ClickTale Ltd., US Patent Pending


window.ClickTaleGlobal = window.ClickTaleGlobal || {};
window.ClickTaleSettings = window.ClickTaleSettings || {};

ClickTaleGlobal.init = ClickTaleGlobal.init || {};
ClickTaleGlobal.scripts = ClickTaleGlobal.scripts || {};


ClickTaleGlobal.scripts.filter = ClickTaleGlobal.scripts.filter || (function () {
	var recordingThreshold = Math.random() * 100;

	return {
		isRecordingApproved: function(percentage) {
			return recordingThreshold <= percentage;
		}
	}
})();
	
		
// Copyright 2006-2018 ClickTale Ltd., US Patent Pending
// PID: 38960



/*browsers exclusion start*/function doOnlyWhen(toDoHandler, toCheckHandler, interval, times, failHandler) {
    if ((!toDoHandler) || (!toCheckHandler)) return;
    if (typeof interval == "undefined") interval = 1000;
    if (typeof times == "undefined") times = 20;

    if (--times < 0 && typeof failHandler === 'function') {
        failHandler();
        return;
    }
    if (toCheckHandler()) {
        toDoHandler();
        return;
    }

    setTimeout(function () { doOnlyWhen(toDoHandler, toCheckHandler, interval, times); }, interval);
}
doOnlyWhen(function () { var ct_UA = ClickTaleDetectAgent(); if (!(((ct_UA.t == ct_UA.IE && ct_UA.v <= 8)))) { (function(){
window.ClickTaleSettings = window.ClickTaleSettings || {};
window.ClickTaleSettings.PTC = window.ClickTaleSettings.PTC || {};
window.ClickTaleSettings.PTC.originalPCCLocation = "P02_PID38960";
var d=!0,e=!1,f=this;var h,k,l,m;function n(){return f.navigator?f.navigator.userAgent:null}m=l=k=h=e;var o;if(o=n()){var p=f.navigator;h=0==o.indexOf("Opera");k=!h&&-1!=o.indexOf("MSIE");l=!h&&-1!=o.indexOf("WebKit");m=!h&&!l&&"Gecko"==p.product}var q=h,r=k,s=m,t=l,v;
a:{var w="",x;if(q&&f.opera)var z=f.opera.version,w="function"==typeof z?z():z;else if(s?x=/rv\:([^\);]+)(\)|;)/:r?x=/MSIE\s+([^\);]+)(\)|;)/:t&&(x=/WebKit\/(\S+)/),x)var A=x.exec(n()),w=A?A[1]:"";if(r){var B,C=f.document;B=C?C.documentMode:void 0;if(B>parseFloat(w)){v=""+B;break a}}v=w}var D={};
function E(a){var c;if(!(c=D[a])){c=0;for(var g=(""+v).replace(/^[\s\xa0]+|[\s\xa0]+$/g,"").split("."),b=(""+a).replace(/^[\s\xa0]+|[\s\xa0]+$/g,"").split("."),u=Math.max(g.length,b.length),y=0;0==c&&y<u;y++){var X=g[y]||"",Y=b[y]||"",Z=RegExp("(\\d*)(\\D*)","g"),aa=RegExp("(\\d*)(\\D*)","g");do{var i=Z.exec(X)||["","",""],j=aa.exec(Y)||["","",""];if(0==i[0].length&&0==j[0].length)break;c=((0==i[1].length?0:parseInt(i[1],10))<(0==j[1].length?0:parseInt(j[1],10))?-1:(0==i[1].length?0:parseInt(i[1],
10))>(0==j[1].length?0:parseInt(j[1],10))?1:0)||((0==i[2].length)<(0==j[2].length)?-1:(0==i[2].length)>(0==j[2].length)?1:0)||(i[2]<j[2]?-1:i[2]>j[2]?1:0)}while(0==c)}c=D[a]=0<=c}return c}var F={};function G(){F[9]||(F[9]=r&&!!document.documentMode&&9<=document.documentMode)};!r||G();!r||G();r&&E("8");!t||E("528");s&&E("1.9b")||r&&E("8")||q&&E("9.5")||t&&E("528");!s||E("8");function H(a,c,g,b,u){a&&c&&("undefined"==typeof g&&(g=1E3),"undefined"==typeof b&&(b=20),0>--b?"function"===typeof u&&u():c()?a():setTimeout(function(){H(a,c,g,b,u)},g))};function I(a){function c(){2==++I.g&&a()}ba(function(){c()});if("function"==typeof ClickTaleIsRecording&&ClickTaleIsRecording()===d)c();else{var g=window.ClickTaleOnRecording||function(){};window.ClickTaleOnRecording=function(){c();return g.apply(this,arguments)}}}I.g=0;function ba(a){function c(){g||(g=d,a())}var g=e;"complete"===document.readyState||"interactive"===document.readyState?c():document.addEventListener&&document.addEventListener("DOMContentLoaded",c,e)}
function ca(a,c){document.addEventListener("mouseup",function(g){a===g.target&&c();document.removeEventListener("mouseup",arguments.callee,e)},e)}function da(a,c){function g(b){document.removeEventListener("touchend",arguments.callee,e);a===b.target&&c()}document.addEventListener("touchend",g,e);document.addEventListener("touchmove",function(b){document.removeEventListener("touchmove",arguments.callee,e);document.removeEventListener("touchend",g,e)},e)}
function J(a,c){var g=K();g&&(J=g.m?da:ca,J(a,c))};function L(a,c){"function"===typeof ClickTaleEvent&&(c?L.f[a]!==d&&(L.f[a]=d,ClickTaleEvent(a)):ClickTaleEvent(a))}L.f={};function M(a){"function"===typeof window.ClickTaleRegisterElementAction&&ClickTaleRegisterElementAction("mouseover",a)}function N(a,c){var g={},b;for(b in a)g[b]=a[b];g.target=c;g.srcElement=c;"function"===typeof window.ClickTaleRegisterElementAction&&ClickTaleRegisterElementAction("click",g)}window.ClickTaleDetectAgent&&window.ClickTaleDetectAgent()&&window.ClickTaleDetectAgent();
function O(a,c){"object"==typeof a&&"string"==typeof c&&(window.ClickTaleContext&&-1!=document.referrer.indexOf(location.hostname)&&window.parent.ct&&window.parent.ct.ElementAddressing&&"function"===typeof window.parent.ct.ElementAddressing.setCustomElementID?window.parent.ct.ElementAddressing.setCustomElementID(a,c):(window.ClickTaleSetCustomElementID=window.ClickTaleSetCustomElementID||function(a,b){a.ClickTale=a.ClickTale||{};a.ClickTale.CustomID=b},window.ClickTaleSetCustomElementID(a,c)))}
function K(){if("function"===typeof ClickTaleDetectAgent){var a=ClickTaleDetectAgent();if(a)return K=function(){return a},K()}return null};function P(a){"function"===typeof ClickTaleExec&&ClickTaleExec(a)}var Q=L,ea=J;var R="",S=document.location.pathname.toLowerCase(),T=[{d:"Windows 10",b:/(Windows 10.0|Windows NT 10.0)/},{d:"Windows 8.1",b:/(Windows 8.1|Windows NT 6.3)/},{d:"Windows 8",b:/(Windows 8|Windows NT 6.2)/},{d:"Windows 7",b:/(Windows 7|Windows NT 6.1)/},{d:"Windows Vista",b:/Windows NT 6.0/},{d:"Windows Server 2003",b:/Windows NT 5.2/},{d:"Windows XP",b:/(Windows NT 5.1|Windows XP)/},{d:"Windows 2000",b:/(Windows NT 5.0|Windows 2000)/},{d:"Windows ME",b:/(Win 9x 4.90|Windows ME)/},{d:"Windows 98",b:/(Windows 98|Win98)/},
{d:"Windows 95",b:/(Windows 95|Win95|Windows_95)/},{d:"Windows NT 4.0",b:/(Windows NT 4.0|WinNT4.0|WinNT|Windows NT)/},{d:"Windows CE",b:/Windows CE/},{d:"Windows 3.11",b:/Win16/},{d:"Android",b:/Android/,e:/Android\s*([^;]*)/},{d:"Open BSD",b:/OpenBSD/},{d:"Sun OS",b:/SunOS/},{d:"Linux",b:/(Linux|X11)/},{d:"iOS",b:/(iPhone|iPad|iPod)/,e:/(?:iPhone|iPad|iPod)[^;\d]+?(\d+(?:\D\d+)?)/},{d:"Mac OS X",b:/Mac OS X/,e:/Mac OS X[^\d]*(\d+(?:_\d+)*)/},{d:"Mac OS",b:/(MacPPC|MacIntel|Mac_PowerPC|Macintosh)/},
{d:"QNX",b:/QNX/},{d:"UNIX",b:/UNIX/},{d:"BeOS",b:/BeOS/},{d:"OS/2",b:/OS\/2/},{d:"Windows Phone",b:/Windows Phone/,e:/Windows Phone[^;\d]+?(\d+(?:\D\d+)?)/},{d:"Search Bot",b:/(gomez|nuhk|Googlebot|Yammybot|Openbot|Slurp|MSNBot|Ask Jeeves\/Teoma|ia_archiver)/i}],U="",V=void 0;function W(a){return 0<a.length?d:e}
function fa(){var a=jQuery(".popular-solutions-container > a");setTimeout(function(){if(1<jQuery(a).length)jQuery(a).each(function(a,b){O(b,"popularSolution_"+a)});else if(1===jQuery(a).length){var c=jQuery(a);O(c[0],"popularSolution_")}},500)}
function ga(){S=document.location.pathname.toLowerCase();U=navigator.userAgent;for(var a=0;a<T.length;a++){var c=T[a];if(c.b.test(U)){V=c.d;c.e&&(a=U.match(c.e))&&a[1]&&(V+=" "+a[1]);break}}if(/(?:documentation\/(articles|samples|templates)|marketplace|case-studies|partners\/directory)/i.test(S)&&-1<S.indexOf("en-us"))jQuery(document).on("input","#MainSearchBox,.wa-textFilter input",function(){var a=jQuery(this),b=a.val()||"";a.is("#MainSearchBox")?P('jQuery("#MainSearchBox").val(unescape("'+escape(b)+
'"));'):a.is(".wa-textFilter input")&&P('jQuery(".wa-textFilter input").val(unescape("'+escape(b)+'"));')});S.match(/en-us\/solutions\/[\w\W]*\//gi)&&(R="Solutions Subpages");if("/en-us/"===S||"/en-us"===S)R="Homepage",V&&-1==V.indexOf("Windows 10")&&Q("Onload | HomePage - Non Win10 user"),fa();V&&Q("Onload | All Pages: OS = "+V);R.length&&Q("Onload | "+R,d);W(jQuery(".msame_Header_picframe"))&&Q("Onload |AllPages - Signed In User");W(jQuery('meta[name="ms.opt_tid"]'))&&(a=jQuery('meta[name="ms.opt_tid"]').attr("content"),
a.length&&Q("Onload | tid: "+a,d));W(jQuery('meta[name="ms.opt_eid"]'))&&(a=jQuery('meta[name="ms.opt_eid"]').attr("content"),a.length&&Q("Onload | eid: "+a,d))}
function ha(){if(!window.ClickTaleFirstPCCGo){window.ClickTaleFirstPCCGo=d;ga();if(jQuery(".sft-target .mscom-link:not(:has(div))").length)for(var a=0;a<jQuery(".sft-target .mscom-link:not(:has(div))").length;a++)if(0<jQuery(".sft-target .mscom-link:not(:has(div)):eq("+a+")").text().length){var c=jQuery(".sft-target .mscom-link:not(:has(div)):eq("+a+")").text().split(" ").join("");O(jQuery(".sft-target .mscom-link:not(:has(div))")[a],c+"Link")}0<jQuery("#msame_si1 a.msame_TxtTrunc").length&&O(jQuery("#msame_si1 a.msame_TxtTrunc")[0],
"SignInUser");jQuery("div#hpfeb15-hero-slideshow:eq(0)").length&&O(jQuery("div#hpfeb15-hero-slideshow")[0],"TopCarouselDiv");jQuery("ul#hpfeb15-hero-slideshow:eq(0)").length&&O(jQuery("ul#hpfeb15-hero-slideshow")[0],"TopCarouselul");jQuery("ul#hpfeb15-hero-slideshow #slide-1:eq(0)").length&&O(jQuery("ul#hpfeb15-hero-slideshow #slide-1")[0],"TopCarouselSlide1il");jQuery("ul#hpfeb15-hero-slideshow #slide-2:eq(0)").length&&O(jQuery("ul#hpfeb15-hero-slideshow #slide-2")[0],"TopCarouselSlide2il");jQuery("ul.menu").on("mousedown",
"a",function(a){ea(a.target,function(){var b=jQuery(a.target);if(W(b.closest(".menu-pop > li > a")))b=b.closest(".menu-pop > li > a"),N(a,b[0]);else if(W(b.closest(".menu-drop >li > a")))b=b.closest(".menu-drop > li > a"),N(a,b[0]);else if(W(b.closest('a[data-event="global-clicked-topnav"]'))){var b=b.closest("ul.menu > li > a"),c=jQuery(b).text();Q("Action| All Pages | "+c,d);N(a,b[0])}})});jQuery(document).on("mousedown",function(a){var b=jQuery(a.target);"Solutions Subpages"===R&&(W(b.closest("#_references a"))?
Q("Action | Solutions Subpage | Reference Architecture interaction",d):W(b.closest('[data-event="solutiondetails-clicked-customerlogo"]'))?Q("Action | Solutions Subpage | Clicked on Customer Logo",d):W(b.closest(".sd-playinsection"))?Q("Action | solution subpage | Clicked on Featured Video",d):W(b.closest(".row-solutions a"))?Q("Action | Solution Subpages | related solution",d):W(b.closest("#related-services a"))?Q("Action | solution subpages | related service or product",d):W(b.closest(".form-replace input"))?
Q("Action | Solution Subpage | Interact with form",d):W(b.closest(".form-navigation button"))?(Q("Action | Solution Subpage | Submit form",d),setTimeout(function(){jQuery(".field-validation-error").filter(":visible").length&&Q("Action | Solution Subpage | Submit form - Validation Error",d)},600)):W(b.closest(".solution-integrators a"))&&Q("Action | Solution Subpage | Partner Logo Interaction",d));if(W(b.closest(".popular-solutions-container > a")))b=b.closest(".popular-solutions-container > a"),0<
b.length&&N(a,b[0]);else if(W(b.closest(".shell-header-dropdown-label a")))Q("Action | All Pages: Clicked on "+b.text().trim()+" Top Navigation bar",d);else if(W(b.closest("UL.shell-header-nav a"))){var c=b.closest("UL.shell-header-nav a");0<c.length&&N(a,c[0]);W(b.closest(".shell-header-dropdown-tab-content a"))&&Q("Action| All Pages |Dropdown Navigation bar 2nd level - Interacted with",d)}else W(b.closest("#srv_shellHeaderMicrosoftLogo"))?Q("Action| All Pages|MS Logo - Clicked",d):W(b.closest(".shell-search-wrapper"))?
Q("Action| All Pages |Search - Interacted with",d):W(b.closest(".shell-header-cart"))?Q("Action| All Pages |Cart - Clicked",d):W(b.closest(".msame_Header"))?Q("Action| All Pages |Sign in - Clicked",d):W(b.closest("#hp-feedback-form-opener"))?Q("Action| All Pages |Site FeedBack - Clicked",d):W(b.closest(".mscom-link.social-icon-link"))?Q("Action| All Pages |Social Media - Clicked",d):W(b.closest(".mscom-footer-productlist li a"))?Q("Action| All Pages |Product site footer - clicked",d):b.closest(".mscom-footer-destinationlink a, .mscom-footer-destinationlink a, .mscom-footer-popularresources a").length?
Q("Action| All Pages |footer links - clicked",d):W(b.closest(".mscom-footer-defaultlink a"))?Q("Action| All Pages | bottom links - clicked",d):W(b.closest("#feedbwSubmit"))?Q("Action| All Pages |Submit feedback clicked",d):W(b.closest(".msame_Header_picframe"))?N(a,b.closest(".msame_Header_picframe img")[0]):W(b.closest("#msame_si1 a.msame_TxtTrunc"))&&N(a,b.closest("#msame_si1 a.msame_TxtTrunc")[0])});if(-1<S.indexOf("/solutions")&&0<jQuery(".solutions-home").length)jQuery(document).on("mousedown",
".logo-text-container",function(a){var b=jQuery(a.target);Q("Action| Azure: Solutions: Clicked on Any Solution",d);b.is("a")||(b=b.closest("a"),0<b.length&&N(a,b[0]))});if("Solutions Subpages"===R)jQuery(document).on("input",".form-replace input",function(){jQuery(this);Q("Action | Solution Subpage | Interact with form",d)});if("/en-us"===document.location.pathname.toLowerCase()||"/en-us/"===document.location.pathname.toLowerCase())jQuery(".next,.prev,.hp-large-carousel img,.box-description .mscom-link").each(function(a,
b){O(b,"custID"+a)}),jQuery(document).mousedown(function(a){var b=jQuery(a.target);W(b.closest(".mini-features.home.row-fluid a"))?Q("Action | Homepage - Consumer products - clicked",d):W(b.closest(".work .CSPvNext a"))?Q("Action | Homepage - For Work Products - Clicked",d):W(b.closest("#hp_heroslide"))?(Q("Action | HomePage - Top Carousel Interacted with.",d),(b.is("img")||b.is(".box-description .mscom-link"))&&M(a)):W(b.closest("#hp_heroslide_sam"))?(Q("Action | Homepage - Interacted with bottom Carousel",
d),(b.is("img")||b.is(".box-description .mscom-link"))&&M(a)):W(b.closest(".hpv19SlimFeature a"))&&(a=jQuery(".hpv19SlimFeature a").text(),Q("Action | Homepage -"+a+"- clicked",d))})}}I(function(){H(ha,function(){return window.jQuery&&"function"===typeof jQuery.fn.on?d:e},250,40)});})(); } }, function () { return (typeof ClickTaleDetectAgent === 'function'); }, 500, 20);


//Signature:Fad2jvF0x5eb45huUWsAsWoWhhD0bNAmVx+RYuLf1fXHWygEbHqsnBQj1VBi2o/LxjVFhe7R5vOJDfMWAjoVxkXO8PIQfBnd6xxqzOTKLa+n1PIN1bzzdKLCSg/J8IWoLgc9qlgt+oc1iilKLugBO8WGGUh0YYjRH21Mq//tuO0=