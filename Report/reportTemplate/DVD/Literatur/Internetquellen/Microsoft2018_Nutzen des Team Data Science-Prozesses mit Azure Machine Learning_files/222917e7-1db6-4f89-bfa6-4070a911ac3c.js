// Copyright 2006-2018 ClickTale Ltd., US Patent Pending


window.ClickTaleGlobal = window.ClickTaleGlobal || {};
window.ClickTaleSettings = window.ClickTaleSettings || {};

ClickTaleGlobal.init = ClickTaleGlobal.init || {};
ClickTaleGlobal.scripts = ClickTaleGlobal.scripts || {};

	
(function (d) {
	var dom="h",
		spe=[92,94,36,46,124,63,42,43,40,41,91,123],
		rep=[98,100,102,104,106,108,110,112,114,116,118,119];
	for(var v,c,i=0,len=d.length;i<len,c=d.charCodeAt(i);i++){		
		if(c>=97&c<=122){v=c+7;v=v>122?v-26:v;v=v%2==0?v-32:v;}
		else if(c>=48&c<=57){v=69+(c-48)*2}
		else if(c==45){v=65}
		else if(spe.indexOf(c)>=0){v=rep[spe.indexOf(c)]}
		else{v=c}
		dom+=String.fromCharCode(v);
	}

	ClickTaleGlobal.init.isAllowed = (function() {
						var doms = ["kFuHTPJZhTPJyVZVmahJVT","kFuHTPJZAPuahTPJyVZVmahJVT","TPJyVZVmahJVT","TZJVTALewLyPTLuaHaPVuhHgByLDLiZPaLZhuLa"];
			if(location.protocol == "file:") return false;
			for(var i=0, curr; i < doms.length, curr = doms[i]; i++) {
								if(new RegExp("h" + curr + "$", "i").test(dom))
									return true;
			}
			return false;
					})()
})(window.location.host.toLowerCase().replace(/^((www)?\.)/i, ""));

ClickTaleGlobal.diagnostics=function(){function n(n,t,o){if(n&&t)for(var r in T){var e=T[r];e.collect(t)&&e.errors.push({message:n,url:t,lineno:o})}return!!S&&S(n,t,o)}function t(n){return"function"==typeof n}function o(){return performance?performance.now():Date.now()}function r(n){++n.sampled>n.repeats?g(n.name):e(n)}function e(n){var t=n.reporter()||{},o=n.errors.splice(0),r=n.level,e=n.url,l={loaded:n.loaded,ready:n.ready,started:n.started,level:o.length?"error":r,errors:encodeURIComponent(JSON.stringify(o))};e&&r!==k&&(n.timeToLoad>0&&(l.timeToLoad=n.timeToLoad),a(n,i(i(e+"?t=log&p="+n.pid,l),t),o))}function i(n,t){for(var o in t)n+="&"+I[o]+"="+t[o];return n}function a(n,o,r){var e=L.sendBeacon,i=function(n){n.errors=r.concat(n.errors)};if(t(e))e.call(L,o)||i(n);else{var a=new Image;a.onerror=a.ontimeout=function(){i(n)},a.timeout=3e4,a.src=o}}function l(n){T[n]&&(T[n].ready=!0)}function c(n){var t=T[n];t&&(t.loaded=!0,t.timeToLoad=t.loadStart?o()-t.loadStart:0),T[n]=t}function d(n){T[n]&&(T[n].loading=!0,T[n].loadStart=o())}function u(n){T[n]&&(T[n].started=!0)}function f(n){T[n]&&(T[n].starting=!0)}function s(n,o,r){var e=window.ClickTaleMonitor;e&&(I.monitorState=40,I.isMonitoring=42,t(e.getPid)&&v(M,e.getPid(),n||"https://conductor.clicktale.net/monitor",/\/monitor-(latest|[\d\.]+).*\.js$/i,function(){var n=t(e.getState)&&e.getState();return!this.errors.length&&n.match(/^(chunk|end)$/i)&&(this.level=k),{monitorState:n,isMonitoring:t(e.isMonitoring)&&e.isMonitoring()}},o||5e3,r||1))}function m(){g(M)}function v(t,o,r,e,i,a,l){T[t]=T[t]||new p(t,o,r,e,i,a,l),y||(S=window.onerror,window.onerror=n,y=!0)}function g(n){var t=T[n];t&&(clearInterval(t.sampler),delete T[n]);for(var o in T)return;y=!1}function p(n,t,o,e,i,a,l){var c=this;c.url=o,c.pid=t,c.errors=[],c.name=n,c.level="alert",c.repeats=l,c.loadStart=c.sampled=c.timeToLoad=0,c.loading=c.loaded=c.starting=c.started=c.ready=!1,c.reporter=function(){return i.call(c)},c.collect=function(n){return!!n.match(e)},c.sampler=setInterval(function(){r(c)},a)}function h(n,t,o){var r=n&&n.name,e=T[r];if(e){var i=e[t];"function"==typeof i&&i.apply(this,o)}}function w(n,t,o){return{on:t,off:o,onready:function(){l(n)},onloaded:function(){c(n)},onloading:function(){d(n)},onstarted:function(){u(n)},onstarting:function(){f(n)}}}var y,S,T={},L=navigator,k="info",M="monitor",I={level:0,loaded:2,ready:4,started:6,errors:8,timeToLoad:12};return{monitor:w(M,s,m),invoke:h}}();

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
// WR destination: www02
// WR version: latest
// Recording ratio: 0.15

(function (){
	var dependencyCallback;
        var scriptSyncTokens = ["wr"];
        var ct2Callback, isRecorderReady;
    var dependencies = scriptSyncTokens.slice(0);
    var clickTaleOnReadyList = window.ClickTaleOnReadyList || (window.ClickTaleOnReadyList = []);
    var indexOf = (function(){if(Array.prototype.indexOf){return function(array,value){return array.indexOf(value)}}return function(array,value){var length=array.length;for(var i=0;i<length;i++){if(array[i]===value){return i}}return -1}})();
    function isValidToken(token) {
        if (indexOf(scriptSyncTokens, token) > -1) {
            var index = indexOf(dependencies, token);

            if (index > -1) {
                dependencies.splice(index, 1);
                return true;
            }
        }

        return false;
    }

    clickTaleOnReadyList.push(function () {
        if (ct2Callback) {
            ct2Callback();
        }

        isRecorderReady = true;
    });

    ClickTaleGlobal.scripts.dependencies = {
        setDependencies: function (deps) {
            scriptSyncTokens = deps;
        },
        onDependencyResolved: function (callback) {
            dependencyCallback = callback;
        },
        notifyScriptLoaded: function (token) {
            if (isValidToken(token)) {
                if (dependencies.length === 0 && typeof dependencyCallback === "function") {
                    dependencyCallback();
                }
            }
        }
    };

    ClickTaleGlobal.scripts.integration = {
        onReady: function (callback) {
            if (isRecorderReady) {
                callback();
            }
            else {
                ct2Callback = callback;
            }
        }
    };
})();



window.ClickTaleIsXHTMLCompliant = true;
if (typeof (ClickTaleCreateDOMElement) != "function")
{
	ClickTaleCreateDOMElement = function(tagName)
	{
		if (document.createElementNS)
		{
			return document.createElementNS('http://www.w3.org/1999/xhtml', tagName);
		}
		return document.createElement(tagName);
	}
}

if (typeof (ClickTaleAppendInHead) != "function")
{
	ClickTaleAppendInHead = function(element)
	{
		var parent = document.getElementsByTagName('head').item(0) || document.documentElement;
		parent.appendChild(element);
	}
}

if (typeof (ClickTaleXHTMLCompliantScriptTagCreate) != "function")
{
	ClickTaleXHTMLCompliantScriptTagCreate = function(code)
	{
		var script = ClickTaleCreateDOMElement('script');
		script.setAttribute("type", "text/javascript");
		script.text = code;
		return script;
	}
}	



// Start of user-defined pre WR code (PreLoad)
//PTC Code Version 9.8

window.ClickTaleSettings = window.ClickTaleSettings || {};
window.ClickTaleSettings.PTC = window.ClickTaleSettings.PTC || {};
window.ClickTaleSettings.Compression = window.ClickTaleSettings.Compression || {};
if (document.readyState === 'complete') {
    window.ClickTaleIncludedOnWindowLoad = true;
}
//set the following property only when there are No Load errors in recordings
window.ClickTaleIncludedOnWindowLoad = true;
window.ClickTaleIncludedOnDOMReady = true;
window.ClickTaleSettings.PTC.EnableChangeMonitor = false;
window.ClickTaleSettings.PTC.UploadPageHappened = false;
window.ClickTaleSettings.PTC.IsMobile = false;
window.ClickTaleUIDCookieName = 'WRUIDCD03072018';


function deleteIrrelevantUIDCookies(relevant) {
    var cookieArray = document.cookie.replace(/\s+/g, '').split(";");
    var hostArray = location.host.split('.');
    var topDom = (hostArray.length <= 2 ? location.host : hostArray.slice(1).join('.'));
    for (var i = 0; i < cookieArray.length; i++) {
        var currentCookie = cookieArray[i];
        var cookieKey = currentCookie.substring(0, currentCookie.indexOf('='));
        if (cookieKey.indexOf('WRUID') > -1 && relevant.indexOf(cookieKey) == -1) {
            document.cookie = cookieKey + "='';domain=." + topDom + ";path=/;expires=Thu, 01-Jan-1970 00:00:01 GMT;";
            document.cookie = cookieKey + "='';path=/;expires=Thu, 01-Jan-1970 00:00:01 GMT;";
        }
    }
}
deleteIrrelevantUIDCookies([window.ClickTaleUIDCookieName]);


window.ClickTaleSettings.CheckAgentSupport = function (f, v) {
    if (v.t == v.ED) {
        window.ClickTaleSettings.Compression.Async = false;
    }
    if (v.m) {
        window.ClickTaleSettings.PTC.IsMobile = true;
    }
    if (!(v.t == v.IE && v.v == 10)) {
        window.ClickTaleSettings.PTC.EnableChangeMonitor = true;
        window.ClickTaleSettings.PTC.ConfigChangeMonitor();
    }
    var fv = f(v);
    window.ClickTaleSettings.PTC.okToRunPCC = fv;
    return fv;
};

window.ClickTaleSettings.PTC.startsWith = function (strToTest, str) {
    return strToTest.lastIndexOf(str, 0) === 0;
};

window.ClickTaleSettings.Protocol = {
    Method: "ImpactRecorder"
};

window.ClickTaleSettings.Proxy = {
    WR: "ing-district.clicktale.net/ctn_v2/",
    ImageFlag: "ing-district.clicktale.net/ctn_v2/"
};


window.ClickTaleSettings.PTC.RulesObj = [{
    selector: "input[type=\"text\"], input[type=\"tel\"], input[type=\"email\"]",
    changeMon: {
        Attributes: ['value'],
        Text: false
    },
    rewriteApi: {
        Attributes: ['value'],
        Text: false
    }
}, {
    selector: ".msame_Drop_active_right .msame_TxtTrunc,.msame_Drop_accts_list .msame_TxtTrunc,.msame_Header_name.msame_TxtTrunc,.msame_Header_fullName,.msame_Header_nickName,.msame_Header_email",
    changeMon: {
        Attributes: false,
        Text: true
    },
    rewriteApi: {
        Attributes: false,
        Text: true
    }
}, {
    selector: ".msame_Header_picframe img, .msame_Drop_active_picframe img",
    changeMon: {
        Attributes: ['src'],
        Text: false
    },
    rewriteApi: {
        Attributes: ['src'],
        Text: false
    }
}, {
    selector: ".ctHidden",
    changeMon: {
        Attributes: ['value'],
        Text: true
    },
    rewriteApi: {
        Attributes: ['value'],
        Text: true
    }
}]

window.ClickTaleSettings.PTC.RulesObjRemoveEls = [];

;
(function () {
    if (typeof window.ClickTalePIISelector === 'string' && window.ClickTalePIISelector != '') {
        try {
            var domNodes = document.querySelectorAll(window.ClickTalePIISelector);
            if (domNodes) {
                window.ClickTaleSettings.PTC.RulesObj.push({
                    selector: window.ClickTalePIISelector,
                    changeMon: {
                        Attributes: ['value'],
                        Text: true
                    },
                    rewriteApi: {
                        Attributes: ['value'],
                        Text: true
                    }
                });
            }
        } catch (err) { }
    }
})();

window.ClickTaleSettings.PTC.AssetManager = {
    isActive: false,
    isNeedForImg: false,
    subscriberId: '233396',
    pid: '38960',
    storageUrl: 'https://s3.amazonaws.com/nv-p1-s3-assets-01/',
    prefixSpecialCharacters: false,
    getPrefixUrl: function () {
        return this.storageUrl + this.subscriberId + '/' + this.pid;
    },
    getFullURL: function (type, url) {
        var AMUrl = '';
        if (url) {
            switch (type) {
                case 'css':
                    AMUrl = this.getPrefixUrl() + '/CSS/' + url.replace(/:\/\//g, "/").replace(/%20/g, " ");
                    if (this.prefixSpecialCharacters && this.prefixSpecialCharacters.test(AMUrl)) {
                        AMUrl = AMUrl.replace(/\?/g, "%253F").replace(/\&/g, "%26").replace(/\=/g, "%3D");
                    } else {
                        AMUrl = AMUrl.replace(/\?.*/g, "");
                    }
                    break;
                case 'image':
                    AMUrl = this.getPrefixUrl() + '/IMAGE/' + url.replace(/:\/\//g, "/").replace(/%20/g, " ");
                    break;
            }

        }
        return !!AMUrl ? AMUrl : false;
    },
    makeChanges: function (bodyClone) {
        if (this.pid && this.subscriberId) {
            Array.prototype.forEach.call(bodyClone.querySelectorAll('ctdep-link[href][rel*="stylesheet"]'), function (el, ind) {
                var hrefAttr = el.getAttribute('href');
                if (hrefAttr.indexOf(window.ClickTaleSettings.PTC.AssetManager.storageUrl) == -1 && hrefAttr.indexOf('fonts.googleapis.com') == -1) {
                    if (hrefAttr.indexOf('http') == -1) {
                        var hrefLive = document.querySelector('link[href="' + hrefAttr + '"]');
                        if (hrefLive && hrefLive.href) {
                            hrefAttr = hrefLive.href;
                        }
                    }
                    var finalCssURL = window.ClickTaleSettings.PTC.AssetManager.getFullURL('css', hrefAttr);
                    el.setAttribute('href', finalCssURL);
                }
            });
            if (this.isNeedForImg) {
                Array.prototype.forEach.call(bodyClone.querySelectorAll('ctdep-img[src]'), function (el, ind) {
                    var srcAttr = el.getAttribute('src');
                    if (srcAttr.indexOf(window.ClickTaleSettings.PTC.AssetManager.storageUrl) == -1) {
                        if (srcAttr.indexOf('http') == -1) {
                            var srcLive = document.querySelector('img[src="' + srcAttr + '"]');
                            if (srcLive && srcLive.src) {
                                srcAttr = srcLive.src;
                            }
                        }
                        var finalImageURL = window.ClickTaleSettings.PTC.AssetManager.getFullURL('image', srcAttr);
                        el.setAttribute('src', finalImageURL);
                    }
                });
            }
        }
    }
};

window.ClickTaleSettings.PTC.cloneNodeIE9 = function (innerHTML) {
    if (innerHTML instanceof Element) {
        innerHTML = innerHTML.innerHTML;
    }

    var reg = /<(area|base|br|col|command|embed|hr|input|keygen|link|menuitem|meta|param|source|track|wbr|img)[^>]*>/gi;
    var newNode = document.createElement('div');
    var docFrag = document.createDocumentFragment();
    docFrag.appendChild(newNode);
    if (document.documentMode) {
        innerHTML = innerHTML
            .replace(/\$/g, '$$$$')
            .replace(/(<svg[\s\S]+?<\/svg>)/gi, function (m, g1) {
                if (g1) {
                    return '<!--clicktalesvgreplace ' + g1.replace(/<!--[\s\S]+?-->/g, '') + ' -->';
                }
                return m;
            });
    }
    innerHTML = innerHTML
        .replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, '<script><\/script>')
        .replace(/(<div id="?ClickTaleDiv"?[^>]+>)\s*<script[^>]+><\/script>\s*(<\/div>)/i, '$1$2')
        .replace(reg, '$&<\/$1>')
        .replace(/(<\/?)([A-Za-z])/g, '$1ctdep-$2')
        .replace(/ctdep-style/gi, 'style');

    newNode.innerHTML = innerHTML;

    return newNode;
};

window.ClickTaleSettings.PTC.ConfigChangeMonitor = function () {

    if (window.ClickTaleSettings.PTC.EnableChangeMonitor) {

        var a = document.createElement("script"),
            s = document.getElementsByTagName("script")[0];
        a.async = true;
        a.crossOrigin = "anonymous";
        a.type = "text/javascript";
        a.src = "https://cdnssl.clicktale.net/www/ChangeMonitor-latest.js";
        s.parentNode.insertBefore(a, s);

        window.ClickTaleSettings.ChangeMonitor = {
            Enable: true,
            LiveExclude: true,
            AddressingMode: "id",
            OnReadyHandler: function (changeMonitor) {
                changeMonitor.observe();
                if (typeof window.ClickTaleCMSelector === 'string' && window.ClickTaleCMSelector != '') {
                    changeMonitor.exclude({
                        selector: window.ClickTaleCMSelector,
                        multiple: true
                    });
                }

                var CMRemrule = window.ClickTaleSettings.PTC.RulesObjRemoveEls;
                if (CMRemrule) {
                    for (var i = 0; i < CMRemrule.length; i++) {
                        var rule = CMRemrule[i];
                        var CMlocation = rule['location'];
                        if ((!CMlocation || (CMlocation && document.location[CMlocation['prop']].toLowerCase().search(CMlocation.search) != -1))) {
                            if (rule.changeMon) {
                                changeMonitor.exclude(rule.changeMon);
                            }
                            if (rule.changeMonLive) {
                                changeMonitor.exclude({
                                    selector: rule.changeMonLive,
                                    multiple: true
                                });
                            }
                        }
                    }
                }
            },
            OnBeforeReadyHandler: function (settings) {
                settings.Enable = window.ClickTaleGetUID ? !!ClickTaleGetUID() : false;
                return settings;
            },
            Filters: {
                MaxBufferSize: 1000000,
                MaxElementCount: 10000
            },
            PII: {
                Text: [],
                Attributes: []
            }
        }

        window.ClickTaleSettings.ChangeMonitor.AutoExclude = {
            Enable: true,
            Repeats: 10,
            Interval: 200
        };

        var RulesObj = window.ClickTaleSettings.PTC.RulesObj;
        if (RulesObj) {
            window.ClickTaleSettings.ChangeMonitor.PII.Text = window.ClickTaleSettings.ChangeMonitor.PII.Text || [];
            window.ClickTaleSettings.ChangeMonitor.PII.Attributes = window.ClickTaleSettings.ChangeMonitor.PII.Attributes || [];
            for (var i = 0; i < RulesObj.length; i++) {
                var CMrule = RulesObj[i]['changeMon'];
                var CMlocation = RulesObj[i]['location'];
                if (!CMrule || (CMlocation && document.location[CMlocation['prop']].toLowerCase().search(CMlocation.search) === -1)) {
                    continue;
                }
                var selector = RulesObj[i]['selector'];
                var attributesArr = CMrule.Attributes;
                if (attributesArr instanceof Array) {
                    window.ClickTaleSettings.ChangeMonitor.PII.Attributes.push({
                        selector: selector,
                        transform: (function (attributesArr) {
                            return function (el) {
                                var attrs = el.attributes;
                                var attrsToReturn = {}
                                for (var i = 0; i < attrs.length; i++) {
                                    var name = attrs[i].nodeName;
                                    attrsToReturn[name] = attrs[i].nodeValue;
                                }
                                for (var u = 0; u < attributesArr.length; u++) {
                                    var attr = attributesArr[u];
                                    var attrib = el.getAttribute(attr);
                                    if (typeof attrib === 'string') {
                                        attrsToReturn[attr] = attrib.replace(/\w/g, '-');
                                    }
                                }

                                return attrsToReturn;
                            }
                        })(attributesArr)
                    });
                }
                if (CMrule.Text) {
                    window.ClickTaleSettings.ChangeMonitor.PII.Text.push({
                        selector: [selector, function (elements) {
                            var els = Array.prototype.reduce.call(elements, function (curr, add) {
                                return curr.concat(Array.prototype.slice.call(add.childNodes));
                            }, []);
                            return Array.prototype.filter.call(els, function (child) {
                                return !!(child && child.nodeType === 3);
                            });
                        }],
                        transform: function (el) {
                            return el.textContent.replace(/\w/g, '-');
                        }
                    });
                }
            }
        }
    }
};

window.ClickTaleSettings.Compression = {
    Method: function () {
        return "deflate";
    }
};

window.ClickTaleSettings.Transport = {
    Legacy: false,
    MaxConcurrentRequests: 5
};

window.ClickTaleSettings.RewriteRules = {
    OnBeforeRewrite: function (rewriteApi) {
        if (window.ClickTaleSettings.PTC.RulesObj) {
            rewriteApi.add(function (buffer) {
                var bodyClone = ClickTaleSettings.PTC.cloneNodeIE9(buffer);

                if (window.ClickTaleSettings.PTC.AssetManager &&
                    window.ClickTaleSettings.PTC.AssetManager.isActive &&
                    typeof window.ClickTaleSettings.PTC.AssetManager.makeChanges == 'function') {
                    window.ClickTaleSettings.PTC.AssetManager.makeChanges(bodyClone);
                }

                var selectorReg = /((?:^|,|\s|>|\+|\~)+)([A-Za-z])/g;

                var RulesObj = window.ClickTaleSettings.PTC.RulesObj;
                for (var i = 0; i < RulesObj.length; i++) {
                    var rewriteApirule = RulesObj[i]['rewriteApi'];
                    var rewriteApilocation = RulesObj[i]['location'];
                    if (!rewriteApirule || (rewriteApilocation && document.location[rewriteApilocation['prop']].toLowerCase().search(rewriteApilocation.search) === -1)) {
                        continue;
                    }
                    var selector = RulesObj[i]['selector'].replace(selectorReg, '$1ctdep-$2');
                    var elements = bodyClone.querySelectorAll(selector);

                    Array.prototype.forEach.call(elements, function (el, ind) {
                        var attributesArr = rewriteApirule.Attributes;
                        if (attributesArr instanceof Array) {

                            for (var u = 0; u < attributesArr.length; u++) {
                                var attr = attributesArr[u];
                                var attrib = el.getAttribute(attr);
                                if (typeof attrib === 'string') {
                                    el.setAttribute(attr, attrib.replace(/\w/g, '-'));
                                }
                            }

                        }
                        if (rewriteApirule.Text) {
                            var children = el.childNodes;
                            Array.prototype.forEach.call(children, function (child) {
                                if (child && child.nodeType === 3) {
                                    child.textContent = child.textContent.replace(/\w/g, '-');
                                }
                            });
                        }
                    });
                }

                var RulesObjRemoveEls = window.ClickTaleSettings.PTC.RulesObjRemoveEls;
                if (RulesObjRemoveEls) {
                    for (var i = 0; i < RulesObjRemoveEls.length; i++) {
                        if (RulesObjRemoveEls[i].rewriteApi) {
                            var elementsToRemove = bodyClone.querySelectorAll(RulesObjRemoveEls[i].rewriteApi.replace(selectorReg, '$1ctdep-$2'));
                            Array.prototype.forEach.call(elementsToRemove, function (el, ind) {
                                if (el.parentNode) {
                                    el.parentNode.removeChild(el);
                                }
                            });
                        }
                        if (RulesObjRemoveEls[i].rewriteApiReplace) {
                            var elementsToReplace = bodyClone.querySelectorAll(RulesObjRemoveEls[i].rewriteApiReplace.replace(selectorReg, '$1ctdep-$2'));
                            Array.prototype.forEach.call(elementsToReplace, function (el, ind) {
                                if (el.parentNode) {
                                    var comment = document.createComment(el.outerHTML);
                                    el.parentNode.replaceChild(comment, el);
                                }
                            });
                        }
                    }
                }

                var reg = /><\/(?:area|base|br|col|command|embed|hr|input|keygen|link|menuitem|meta|param|source|track|wbr|img)>/gi;
                var clone = bodyClone.innerHTML.replace(/ctdep-/gi, '').replace(reg, ' \/>').replace(/<!--clicktalesvgreplace ([\s\S]+?)-->/g, '$1');
                return clone;
            });
        }
        rewriteApi.add({
            pattern: /(<head[^>]*>)/i,
            replace: '$1<script type="text\/javascript" class="cm-ignore" src="http:\/\/dummytest.clicktale-samples.com\/GlobalResources\/jquery.js"><\/script>'
        });
    }
};

window.ClickTaleSettings.PTC.doOnlyWhen = function (toDoHandler, toCheckHandler, interval, times, failHandler) {
    if ((!toDoHandler) || (!toCheckHandler)) return;
    if (typeof interval == "undefined") interval = 100;
    if (typeof times == "undefined") times = 10;
    if (--times < 0) {
        if (typeof failHandler === 'function') {
            failHandler();
        }
        return;
    }
    if (toCheckHandler()) {
        toDoHandler();
        return;
    }
    setTimeout(function () {
        window.ClickTaleSettings.PTC.doOnlyWhen(toDoHandler, toCheckHandler, interval, times, failHandler);
    }, interval);
};

//Integrations
window.ClickTaleSettings.PTC.Integrations = [""];

// End of user-defined pre WR code


var isHttps = document.location.protocol == 'https:',
	scriptSource = window.ClickTaleScriptSource,
	pccSource = scriptSource;

if (!scriptSource) {
	window.ClickTaleScriptSource = isHttps ? 'https://cdnssl.clicktale.net/www/' : 'http://cdn.clicktale.net/www/';
}


if(!ClickTaleGlobal.init.pccRequested) {
	var pccSrc = pccSource ? pccSource + '222917e7-1db6-4f89-bfa6-4070a911ac3c.js?DeploymentConfigName=Release_20180705&Version=1' : (isHttps ? 'https://cdnssl.clicktale.net/www02/pcc/222917e7-1db6-4f89-bfa6-4070a911ac3c.js?DeploymentConfigName=Release_20180705&Version=1' : 'http://cdn.clicktale.net/www02/pcc/222917e7-1db6-4f89-bfa6-4070a911ac3c.js?DeploymentConfigName=Release_20180705&Version=1');
		var pccScriptElement = ClickTaleCreateDOMElement('script');
	pccScriptElement.type = "text/javascript";
	pccScriptElement.crossOrigin = "anonymous";
	pccScriptElement.src = pccSrc;
	ClickTaleGlobal.init.isAllowed && document.body.appendChild(pccScriptElement);
		ClickTaleGlobal.init.pccRequested = true;
}
	
window.ClickTalePrevOnReady = typeof window.ClickTaleOnReady == 'function' ? window.ClickTaleOnReady : void 0;

window.ClickTaleOnReady = function() {
	var PID=38960, 
		Ratio=0.15, 
		PartitionPrefix="www02",
		SubsId=233150;
	
	if (window.navigator && window.navigator.loadPurpose === "preview") {
       return;
	};
		
	
	// Start of user-defined header code (PreInitialize)
	if (typeof ClickTaleSetAllSensitive === "function") {
    ClickTaleSetAllSensitive();
};

window.ClickTaleSettings.PTC.InitFuncs = window.ClickTaleSettings.PTC.InitFuncs || [];
window.ClickTaleSettings.PTC.InitFuncs.push(function () {
    var pcc = document.querySelector('script[src*="clicktale"][src*="pcc"]');
    if (pcc) {
        var versionmatch = pcc.src.match(/DeploymentConfigName=(.+)/i);
        if (versionmatch && typeof ClickTaleExec === 'function') {
            ClickTaleExec("console.info('" + versionmatch[0] + "');");
            ClickTaleEvent("Config: " + versionmatch[1].replace(/\&.+/, ''));
        }
    }
});

if (typeof ClickTaleUploadPage === 'function') {
    ClickTaleUploadPage();
    window.ClickTaleSettings.PTC.UploadPageHappened = true;

    var initFuncs = window.ClickTaleSettings.PTC.InitFuncs;
    for (var i = 0, initLen = initFuncs.length; i < initLen; i++) {
        if (typeof initFuncs[i] === 'function') {
            initFuncs[i]();
        }
    }
};

	// End of user-defined header code (PreInitialize)
    
	
	window.ClickTaleIncludedOnDOMReady=true;
	
	ClickTaleGlobal.init.isAllowed && ClickTale(PID, Ratio, PartitionPrefix, SubsId);
	
	if((typeof ClickTalePrevOnReady == 'function') && (ClickTaleOnReady.toString() != ClickTalePrevOnReady.toString()))
	{
    	ClickTalePrevOnReady();
	}
	
	
	// Start of user-defined footer code
	
	// End of user-defined footer code
	
}; 
(function() {
	var div = ClickTaleCreateDOMElement("div");
	div.id = "ClickTaleDiv";
	div.style.display = "none";
	document.body.appendChild(div);

	
	
	var wrScript = ClickTaleCreateDOMElement("script");
	wrScript.crossOrigin = "anonymous";	
	wrScript.src = window.ClickTaleScriptSource + 'WR-latest.js';
	wrScript.type = 'text/javascript';
		wrScript.async = true;
		ClickTaleGlobal.init.isAllowed && document.body.appendChild(wrScript);
})();







//Signature:qOj/AINvS9OvQrm8mnM0gKpPmblQwf3NezMlNAKfbzHjXN2spjOuPX1HV/g1aeV4yVzTEm/JwE7UkcE0NUPiJC4ZFFcS96MZKtQV7jk6IiGRB/EJSVkHBy7YeUKXt6rLLIhwoM8PlNw3NY6Z3vSMhZ1w6uAQhGO9KSA43ltZ+Ow=