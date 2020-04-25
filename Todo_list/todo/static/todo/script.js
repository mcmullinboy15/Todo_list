var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {

        title: "Andrew's TODO list",
        time: "",
        user_id: user_id,
        user: "",
        background_url: "",

    },

    methods: {
        getAllUserData(id) {
            fetch("/todo/"+id+"/api/")
                .then(response => response.json())
                .then(json => {
                    console.log(json)
                    app.user = json
                })

        },

        getTimestamp() {
            var date = new Date();
            d = date.getMonth() + "/";
            d += date.getDate() + "/";
            d += date.getFullYear() + ", ";
            hour = date.getHours()
            d += hour + ":";
            d += date.getMinutes() + ":";
            d += date.getSeconds() + " ";
            d += (hour >= 12) ? ' P.M.' : ' A.M.';
            //TODO I don't know if this edited is is working

            return d


        },
        toggle(ev) {
            var el = ev.target

//            if(el.id == "") {
//                el = el.parentNode
//            }
//            if(el.id == "") {
//                el = el.parentNode
//            }
            while(el.id != ""){
                el = el.parentNode
            }
            //TODO I don't know if this while is working

            var cla = el.getAttribute('class').toString()

            if (cla.includes('black')){
                el.setAttribute('class','stuff-box green');
                app.neutral -= 1
                app.likely += 1

            }else if(cla.includes('green')){
                el.setAttribute('class','stuff-box red')
                app.likely -= 1
                app.unlikely += 1

            }else if(cla.includes('red')){
                el.setAttribute('class','stuff-box black')
                app.unlikely -= 1
                app.neutral += 1
            }
        },

        toggle_sidebar() {

            var el = document.getElementById('sidebar')
            el.classList.toggle('active');

        },

        toggle_active(ev) {
            var el = ev.target
            console.log(el)



            el.classList.toggle('active');

//            while (!el.id.includes('list_box_')) {
//                    el = el.parentNode
//            }

            var children = el.children
            console.log(children)
            for (var child of children) {
                console.log(child)
                child.classList.toggle('disappear')

            }
        },

        isDisappeared(ev){
//            console.log(ev)
//            if(ev.classList.contains('disappear')){
//                return false
//            }else{
//                return true
//            }
        }
    },

    computed: {



    }


})

app.getAllUserData(user_id)
app.time = app.getTimestamp()

fetch("https://api.nasa.gov/planetary/apod?api_key=lXdVWNTa2v5NsPcScU6b9bfVNAMeM9MfN4Fu6EWf")
.then(response => response.json())
.then(json => {
    app.background_url = json.url;
    console.log(app.background_url)
})

//Vue.component('sidebar', {
//    props: ['']
//  data: function () {
//    return {
//      count: 0
//    }
//  },
//  template: '<nav id="sidebar" class="sidebar-box sidebar-color">'\
//            '   <div class="sidebar-header">'\
//            '      <h3>Bootstrap Sidebar</h3>'\
//            '      <strong onclick="toggle_sidebar()">BS</strong>'\
//            '   </div>'\
//
//            '   <ul class="list-unstyled components">'\
//            '       <li class="active">'\
//            '           <a href="#" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">'\
//            '                <i class="fas fa-home"></i>'\
//            '                    <p>Home</p>'\
//            '           </a>'\
//            '            <ul class="collapse list-unstyled" id="homeSubmenu">'\
//            '                <li>'\
//            '                    <a href="#3">Home 1</a>'\
//            '                </li>'\
//            '                <li>'\
//            '                    <a href="#6">Home 2</a>'\
//            '               </li>'\
//            '               <li>'\
//            '                   <a href="#9">Home 3</a>'\
//            '               </li>'\
//            '           </ul>'\
//            '       </li>'\
//            '       <li>'\
//            '           <a href="#_20">'\
//            '               <i class="fas fa-briefcase"></i>'\
//            '                   <p>About</p>'\
//            '           </a>'\
//            '           <a href="#25" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">'\
//            '               <i class="fas fa-copy"></i>'\
//            '                   <p>Pages</p>'\
//            '           </a>'\
//            '           <ul class="collapse list-unstyled" id="pageSubmenu">'\
//            '               <li>'\
//            '                   <a href="#28">Page 1</a>'\
//            '               </li>'\
//            '               <li>'\
//            '                   <a href="#31">Page 2</a>'\
//            '               </li>'\
//            '               <li>'\
//            '                   <a href="#34">Page 3</a>'\
//            '               </li>'\
//            '           </ul>'\
//            '       </li>'\
//            '   </ul>'\
//            '</nav>'
//})