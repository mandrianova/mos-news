(function(e){function t(t){for(var n,r,l=t[0],s=t[1],c=t[2],d=0,v=[];d<l.length;d++)r=l[d],Object.prototype.hasOwnProperty.call(o,r)&&o[r]&&v.push(o[r][0]),o[r]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(e[n]=s[n]);u&&u(t);while(v.length)v.shift()();return i.push.apply(i,c||[]),a()}function a(){for(var e,t=0;t<i.length;t++){for(var a=i[t],n=!0,l=1;l<a.length;l++){var s=a[l];0!==o[s]&&(n=!1)}n&&(i.splice(t--,1),e=r(r.s=a[0]))}return e}var n={},o={app:0},i=[];function r(t){if(n[t])return n[t].exports;var a=n[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,r),a.l=!0,a.exports}r.m=e,r.c=n,r.d=function(e,t,a){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(r.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)r.d(a,n,function(t){return e[t]}.bind(null,n));return a},r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],s=l.push.bind(l);l.push=t,l=l.slice();for(var c=0;c<l.length;c++)t(l[c]);var u=s;i.push([0,"chunk-vendors"]),a()})({0:function(e,t,a){e.exports=a("56d7")},"034f":function(e,t,a){"use strict";a("85ec")},"4b45":function(e,t,a){e.exports=a.p+"img/dudaism.94770eaa.gif"},"56d7":function(e,t,a){"use strict";a.r(t);a("e260"),a("e6cf"),a("cca6"),a("a79d");var n=a("bc3a"),o=a.n(n),i=a("2b0e"),r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-app",[a("router-view")],1)},l=[],s={components:{},name:"App",data:function(){return{}}},c=s,u=(a("034f"),a("2877")),d=a("6544"),v=a.n(d),m=a("7496"),p=Object(u["a"])(c,r,l,!1,null,null,null),f=p.exports;v()(p,{VApp:m["a"]});var h=a("8c4f"),g=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("hello-world")},b=[],_=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("top-bar"),a("div",[a("h5",[e._v(e._s(e.msg))])])],1)},y=[],x=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app-bar",{attrs:{app:"",color:"white",flat:""}},[n("v-container",{staticClass:"py-0 fill-height"},[n("v-avatar",[n("img",{attrs:{src:a("4b45"),alt:"Dude"}})]),e._l(e.links,(function(t){return n("v-btn",{key:t,attrs:{text:""}},[n("router-link",{attrs:{to:{name:t}}},[e._v(e._s(t))])],1)})),n("v-spacer"),n("v-responsive",{attrs:{"max-width":"260"}},[n("v-text-field",{attrs:{dense:"",flat:"","hide-details":"",rounded:"","solo-inverted":""}})],1)],2)],1)},w=[],V={name:"TopBar",data:function(){return{links:["recommendations","markup","documentation","about"]}}},k=V,C=a("40dc"),T=a("8212"),j=a("8336"),O=a("a523"),S=a("6b53"),D=a("2fa4"),E=a("8654"),A=Object(u["a"])(k,x,w,!1,null,null,null),P=A.exports;v()(A,{VAppBar:C["a"],VAvatar:T["a"],VBtn:j["a"],VContainer:O["a"],VResponsive:S["a"],VSpacer:D["a"],VTextField:E["a"]});var $={components:{TopBar:P},name:"Ping",data:function(){return{msg:"Hello"}}},B=$,I=Object(u["a"])(B,_,y,!1,null,null,null),M=I.exports,N={name:"Home",components:{HelloWorld:M}},L=N,R=Object(u["a"])(L,g,b,!1,null,null,null),H=R.exports,q=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"recommendations"}},[a("top-bar"),a("rec-input")],1)},z=[],F=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-main",{staticClass:"grey lighten-3"},[a("v-container",[a("v-row",[a("v-col",{attrs:{md:"10"}},[a("v-sheet",{attrs:{"min-height":"80vh",rounded:"lg"}},[a("v-navigation-drawer",{attrs:{right:"",absolute:""}},[a("v-container",[a("div",{staticClass:"my-3"},[e._v("Input Panel")]),a("v-divider"),a("div",{staticClass:"my-6"},e._l(e.payload,(function(t){return a("v-text-field",{key:t.name,attrs:{label:t.name,dense:"",outlined:""},model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"p.value"}})})),1),e.executionTime>0?a("h6",[e._v(" Execution time: ")]):e._e(),e._v(" "+e._s(e.executionTime)+" sec"),a("br"),a("br"),a("div",{staticClass:"my-3"},[a("v-btn",{attrs:{color:"secondary"},on:{click:e.callApi}},[e._v(" Submit ")])],1)],1)],1),a("v-container",{attrs:{id:"main"}},[a("v-row",[a("v-col",{attrs:{md:"6"}},[a("h3",[e._v("Recommendations")]),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:e.headers,items:e.recommendations,loading:e.loading,"loading-text":"Loading... Please wait"}})],1),a("v-col",{attrs:{md:"6"}},[e.history?a("h3",[e._v("History")]):e._e(),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:e.headers,items:e.history,loading:e.loading,"loading-text":"Loading... Please wait"}})],1)],1)],1)],1)],1)],1)],1)],1)},J=[],G=a("ade3"),U=a("5530"),W=(a("d3b7"),a("b0c0"),{name:"rec-input",data:function(){return{payload:[{name:"user_id",value:20,type:"int"}],loading:!1,headers:[{text:"id",value:"id"},{text:"title",value:"title"},{text:"date",value:"date"}],recommendations:[{id:248,title:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!",date:"2021-08-16 08:00"}],history:[{id:1,title:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!",date:"2021-08-16 08:00"}],executionTime:null}},methods:{callApi:function(){var e=this,t=Date.now();this.loading=!0;var a=this.payload.reduce((function(e,t){return Object(U["a"])(Object(U["a"])({},e),{},Object(G["a"])({},t.name,t.value))}),{});console.log("sending payload",this.payload),o.a.get("/recommendations/".concat(a.user_id),this.payload).then((function(a){console.log("response",a),e.recommendations=a.data.recommendations,e.history=a.data.history,e.loading=!1;var n=Date.now();console.log(n);var o=(n-t)/1e3;e.executionTime=o})).catch((function(e){return console.log(e)}))}}}),K=W,Q=(a("96da"),a("62ad")),X=a("8fea"),Y=a("ce7e"),Z=a("f6c4"),ee=a("f774"),te=a("0fd9"),ae=a("8dd9"),ne=Object(u["a"])(K,F,J,!1,null,null,null),oe=ne.exports;v()(ne,{VBtn:j["a"],VCol:Q["a"],VContainer:O["a"],VDataTable:X["a"],VDivider:Y["a"],VMain:Z["a"],VNavigationDrawer:ee["a"],VRow:te["a"],VSheet:ae["a"],VTextField:E["a"]});var ie={components:{TopBar:P,RecInput:oe}},re=ie,le=Object(u["a"])(re,q,z,!1,null,null,null),se=le.exports,ce=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"markup"},[a("top-bar"),a("markup-input")],1)},ue=[],de=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-main",{staticClass:"grey lighten-3"},[a("v-container",[a("v-row",{staticClass:"justify-center"},[a("v-col",{attrs:{md:"6"}},[a("v-sheet",{attrs:{"min-height":"80vh",rounded:"lg"}},[a("v-navigation-drawer",{attrs:{right:"",absolute:""}},[a("v-container",[a("div",{staticClass:"my-3"},[e._v("Input Panel")]),a("v-divider"),a("div",{staticClass:"my-4"},e._l(e.payload,(function(t){return a("v-textarea",{key:t.name,attrs:{label:t.name,dense:"",outlined:""},model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"p.value"}})})),1),e.executionTime>0?a("h6",[e._v(" Execution time: ")]):e._e(),e._v(" "+e._s(e.executionTime)+" sec"),a("br"),a("div",{staticClass:"my-3"},[a("v-btn",{attrs:{color:"secondary"},on:{click:e.callApi}},[e._v(" Submit ")])],1)],1)],1),a("v-container",{attrs:{id:"main"}},[a("v-row",[a("v-col",{attrs:{md:"6"}},[a("h5",{staticClass:"text-left"},[e._v("TAGS")]),a("v-list",{attrs:{dense:""}},e._l(e.tags,(function(t){return a("v-list-item",{key:t},[e._v(" "+e._s(t)+" ")])})),1)],1),a("v-col",{attrs:{md:"6"}},[a("h5",{staticClass:"text-left"},[e._v("SPHERES")]),a("v-list",{attrs:{dense:""}},e._l(e.spheres,(function(t){return a("v-list-item",{key:t},[e._v(" "+e._s(t)+" ")])})),1)],1)],1)],1)],1)],1)],1)],1)],1)},ve=[],me={name:"markup-input",data:function(){return{payload:[{name:"title",value:"Бесстрашные бойцы и сладкоежки: в Московском зоопарке поселились медоеды"},{name:"preview_text",value:"Медоеды известны своей смелостью. В случае если их жизни что-то угрожает, они без колебаний идут в атаку. Они запросто могут напасть на льва, леопарда и буйвола, им нипочем яд кобры и скорпиона."},{name:"full_text",value:"Один из самых известных отморозков животного мира. Только медоед способен вести схватку, один против шести львов. Есть королевских кобр. Периодически драться с леопардами. Он имеет настолько сильную иммунную систему, что даже после смертельного укуса кобры он просто засыпает, а проснувшись дальше продолжает, есть эту же кобру."}],loading:!1,tags:[],spheres:[],results:{},executionTime:null}},methods:{callApi:function(){var e=this,t=Date.now();this.loading=!0;var a=this.payload.reduce((function(e,t){return Object(U["a"])(Object(U["a"])({},e),{},Object(G["a"])({},t.name,t.value))}),{});console.log("performing API query",a),o.a.post("/auto_markup/generate_markups",a).then((function(a){console.log("response",a.data),e.tags=a.data.tags,e.spheres=a.data.spheres,e.results=a.data,e.loading=!1;var n=Date.now(),o=(n-t)/1e3;e.executionTime=o})).catch((function(e){return console.log(e)}))}}},pe=me,fe=(a("f97c"),a("8860")),he=a("da13"),ge=a("a844"),be=Object(u["a"])(pe,de,ve,!1,null,null,null),_e=be.exports;v()(be,{VBtn:j["a"],VCol:Q["a"],VContainer:O["a"],VDivider:Y["a"],VList:fe["a"],VListItem:he["a"],VMain:Z["a"],VNavigationDrawer:ee["a"],VRow:te["a"],VSheet:ae["a"],VTextarea:ge["a"]});var ye,xe,we={components:{TopBar:P,MarkupInput:_e}},Ve=we,ke=Object(u["a"])(Ve,ce,ue,!1,null,null,null),Ce=ke.exports,Te={},je=Object(u["a"])(Te,ye,xe,!1,null,null,null),Oe=je.exports,Se=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("top-bar"),a("div",[a("v-container",{staticClass:"grey lighten-5 m-5 p-lg-5",staticStyle:{height:"1000px"}},[a("v-row",{staticClass:"justify-content-center m-lg-5"},[e._l(e.zonderTeam,(function(t){return[a("v-card",{key:t.id,staticClass:"mx-auto",attrs:{width:"260",outlined:"",tile:""}},[a("v-img",{key:t.id,attrs:{src:t.img,height:"300px"}}),a("v-card-title",[e._v(" "+e._s(t.fullName)+" ")]),a("v-card-subtitle",[e._v(" "+e._s(t.role)+" ")]),a("v-card-actions",[a("v-btn",{attrs:{color:"grey lighten-2",text:""}},[e._v(" Explore ")]),a("v-spacer"),a("v-btn",{attrs:{icon:""},on:{click:function(t){e.show=!e.show}}},[a("v-icon",[e._v(e._s(e.show?"mdi-chevron-up":"mdi-chevron-down"))])],1)],1),a("v-expand-transition",[a("div",{directives:[{name:"show",rawName:"v-show",value:e.show,expression:"show"}]},[a("v-divider"),a("v-card-text",[e._v(" "+e._s(t.tel)+" "+e._s(t.info)+" "+e._s(t.img)+" ")])],1)])],1)]}))],2)],1)],1)],1)},De=[],Ee={data:function(){return{show:!1,zonderTeam:[{id:1,fullName:"Nikita Stegura",role:"Developer",tel:"+7 (909) 920-99-94",img:"../assets/nikita.png",motto:"",info:""},{id:2,fullName:"Margo Andrianova",role:"Team Lead",tel:"+7 (916) 661-94-65",img:"../assets/margo.png",motto:"",info:""},{id:3,fullName:"Indiko Dzhalagonia",role:"Data Scientist",tel:"+7 (999) 989-26-85",img:"../assets/nick.png",motto:"",info:""},{id:4,fullName:"Denis Volchugin",role:"Developer",tel:"+7 (985) 965-11-87",img:"../assets/den.png",motto:"",info:"4.434.682.001th Man on Earth"}]}},components:{TopBar:P}},Ae=Ee,Pe=a("b0af"),$e=a("99d9"),Be=a("0789"),Ie=a("132d"),Me=a("adda"),Ne=Object(u["a"])(Ae,Se,De,!1,null,null,null),Le=Ne.exports;v()(Ne,{VBtn:j["a"],VCard:Pe["a"],VCardActions:$e["a"],VCardSubtitle:$e["b"],VCardText:$e["c"],VCardTitle:$e["d"],VContainer:O["a"],VDivider:Y["a"],VExpandTransition:Be["a"],VIcon:Ie["a"],VImg:Me["a"],VRow:te["a"],VSpacer:D["a"]}),i["a"].use(h["a"]);var Re=[{path:"/",name:"Home",component:H},{path:"/about",name:"about",component:Le},{path:"/recommendations",name:"recommendations",component:se},{path:"/markup",name:"markup",component:Ce},{path:"/documentation",name:"documentation",component:Oe}],He=new h["a"]({mode:"history",base:"/",routes:Re}),qe=He,ze=a("f309");a("bf40");i["a"].use(ze["a"]);var Fe=new ze["a"]({});i["a"].config.productionTip=!1,o.a.defaults.withCredentials=!1,o.a.defaults.baseURL="http://localhost:80/",new i["a"]({router:qe,vuetify:Fe,render:function(e){return e(f)}}).$mount("#app")},7412:function(e,t,a){},"85ec":function(e,t,a){},"96da":function(e,t,a){"use strict";a("7412")},aa97:function(e,t,a){},f97c:function(e,t,a){"use strict";a("aa97")}});
//# sourceMappingURL=app.e2f1e23e.js.map