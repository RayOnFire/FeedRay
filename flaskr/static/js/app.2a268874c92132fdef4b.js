webpackJsonp([0,2],[,function(e,t,n){var s=n(0)(n(13),n(6),null,null);e.exports=s.exports},,function(e,t,n){var s=n(0)(n(14),n(7),null,null);e.exports=s.exports},function(e,t,n){var s=n(0)(n(15),n(9),null,null);e.exports=s.exports},function(e,t,n){n(10);var s=n(0)(n(16),n(8),null,null);e.exports=s.exports},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("hello"),e._v(" "),n("div",{staticClass:"container"},[n("div",{staticClass:"row"},[n("div",{staticClass:"col s8"},[n("timeline")],1),e._v(" "),n("div",{staticClass:"col s4"},[n("github-trend")],1)])])],1)},staticRenderFns:[]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement;e._self._c||t;return e._m(0)},staticRenderFns:[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"github-trend"}},[n("div",{staticClass:"card"},[n("div",{staticClass:"card-content"},[n("span",{staticClass:"card-title"},[e._v("Github Trend")]),e._v(" "),n("table",[n("thead",[n("tr",[n("th",[e._v("Name")]),e._v(" "),n("th",[e._v("Stars")]),e._v(" "),n("th",[e._v("Repo")])])]),e._v(" "),n("tbody",[n("tr",[n("td",[e._v("Vuejs")]),e._v(" "),n("td",[e._v("10000")]),e._v(" "),n("td",[e._v("Vuejs")])])])])])])])}]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"timeline"}})},staticRenderFns:[]}},function(e,t){e.exports={render:function(){var e=this,t=e.$createElement;e._self._c||t;return e._m(0)},staticRenderFns:[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("nav",[n("div",{staticClass:"nav-wrapper"},[n("a",{staticClass:"brand-logo",attrs:{href:"#"}},[e._v("Logo")]),e._v(" "),n("div",{staticClass:"container"},[n("ul",{staticClass:"right hide-on-med-and-down",attrs:{id:"nav-mobile"}},[n("li",[n("a",{attrs:{href:"login"}},[e._v("Login")])])])])])])}]}},function(e,t){},,,function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=n(4),a=n.n(s),r=n(5),o=n.n(r),i=n(3),l=n.n(i);t.default={name:"app",components:{Hello:a.a,Timeline:o.a,GithubTrend:l.a}}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={name:"githubTrend"}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={name:"hello",components:{},data:function(){return{msg:"Welcome to Your Vue.js App"}},methods:{checkLogin:function(){}}}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={name:"timeline",data:function(){return{page:1}},methods:{makeCard:function(e,t){var n=t.title,s=t.body,a=t.avatar,r="#",o=t.username;e.innerHTML+='<div class="row"><div class="col s12"><a href="'+r+'" class="card-panel hoverable"><div class="user"><img class="responsive-img avatar" src="'+a+'"/><div class="username">'+o+'</div></div><div class="content"><div><h5>'+n+"</h5></div><div>"+s+"</div></div></a></div></div>"},loadXMLDoc:function(e,t){var n=new XMLHttpRequest;n.onreadystatechange=function(){n.readyState===XMLHttpRequest.DONE&&(200===n.status?t(n.responseText):400===n.status?alert("There was an error 400"):alert(n.status))},n.open("GET",e,!0),n.send()},scrollToBottom:function(e){window.onscroll=function(t){window.innerHeight+window.pageYOffset>=document.body.offsetHeight&&e()}},getFeedAndMakeCard:function(){window.onscroll=null;var e=document.getElementById("timeline"),t=this.page,n=this;this.loadXMLDoc("feed?page="+t,function(t){var s=JSON.parse(t);0===s.count&&(alert("No more content~"),window.onscroll=null);for(var a=0;a<s.posts_list.length;a++)n.makeCard(e,s.posts_list[a]),n.scrollToBottom(n.getFeedAndMakeCard)}),this.page+=1}},mounted:function(){var e=(document.getElementById("timeline"),this);this.getFeedAndMakeCard(),this.scrollToBottom(function(){window.onscroll=null,e.page+=1,console.log(e.page),e.getFeedAndMakeCard()})}}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=n(2),a=n.n(s),r=n(1),o=n.n(r);new a.a({el:"#app",template:"<App/>",components:{App:o.a}})}],[17]);