var app = new Vue({
    el: '#app',
    data: {
        title: "Andrew's TODO list",
        background_url: "",
    },

    methods: {
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



            el.classList.toggle('active');

            while (!el.id.includes('list_box_')) {
                    el = el.parentNode
            }

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
    }
})

//fetch("https://api.nasa.gov/planetary/apod?api_key=lXdVWNTa2v5NsPcScU6b9bfVNAMeM9MfN4Fu6EWf")
//.then(response => response.json())
//.then(json => {
//    app.background_url = json.url;
//})