var title = document.querySelector('title').textContent = "This is Andrew's New Title";


var wrapper = document.createElement('div')
wrapper.setAttribute('class', 'wrapper')
document.body.appendChild(wrapper)


var sidebar = document.createElement('nav')
sidebar.id = 'sidebar'
//sidebar.setAttribute('class','active')

var header = document.createElement('div')
header.setAttribute('class', 'sidebar-header')
var sidebar_title = document.createElement('h3')
sidebar_title.textContent='Bootstrap Sidebar'
var BS_strong = document.createElement('strong')
BS_strong.textContent='BS'
header.appendChild(sidebar_title)
header.appendChild(BS_strong)
sidebar.appendChild(header)

var list = document.createElement('ul')
list.setAttribute('class', 'list-unstyled components')
var dumb_heading = document.createElement('p')
dumb_heading.textContent = 'Dummy Heading'
list.appendChild(dumb_heading)
var li1 = document.createElement('li')
li1.setAttribute('class', 'active')
var home_link = document.createElement('a')
home_link.setAttribute('href', '#')
home_link.setAttribute('data-toggle', "collapse")
home_link.setAttribute('aria-expanded', "false")
home_link.setAttribute('class', 'dropdown-toggle')
var i_vas = document.createElement('i')
i_vas.setAttribute('class', 'fas fa-home')
home_link.appendChild(i_vas)
i_vas.textContent='Home'
li1.appendChild(home_link)
var subHome_list = document.createElement('ul')
subHome_list.id = '#homeSubmenu'
subHome_list.setAttribute('class', 'collapse list-unstyled')
var home_1 = document.createElement('li')
var link_1 = document.createElement('a')
link_1.setAttribute('href', '#')
link_1.textContent = 'Home 1'
home_1.appendChild(link_1)
subHome_list.appendChild(home_1)
var home_2 = document.createElement('li')
var link_2 = document.createElement('a')
link_2.setAttribute('href', '#')
link_2.textContent = 'Home 2'
home_2.appendChild(link_2)
subHome_list.appendChild(home_2)
var home_3 = document.createElement('li')
var link_3 = document.createElement('a')
link_3.setAttribute('href', '#')
link_3.textContent = 'Home 3'
home_3.appendChild(link_3)
subHome_list.appendChild(home_3)
li1.appendChild(subHome_list)
list.appendChild(li1)
var about_li = document.createElement('li')
var about_link = document.createElement('a')
about_link.setAttribute('href', '#')
about_link.textContent = 'About'
about_li.appendChild(about_link)
list.appendChild(about_li)

var li3 = document.createElement('li')
li3.setAttribute('class', 'active')
var home_link = document.createElement('a')
home_link.textContent = 'Pages'
home_link.setAttribute('href', '#')
home_link.setAttribute('data-toggle', "collapse")
home_link.setAttribute('aria-expanded', "false")
home_link.setAttribute('class', 'dropdown-toggle')
li3.appendChild(home_link)
var subHome_list = document.createElement('ul')
subHome_list.id = '#pageSubmenu'
subHome_list.setAttribute('class', 'collapse list-unstyled')
var home_1 = document.createElement('li')
var link_1 = document.createElement('a')
link_1.setAttribute('href', '#')
link_1.textContent = 'Home 1'
home_1.appendChild(link_1)
subHome_list.appendChild(home_1)
var home_2 = document.createElement('li')
var link_2 = document.createElement('a')
link_2.setAttribute('href', '#')
link_2.textContent = 'Home 2'
home_2.appendChild(link_2)
subHome_list.appendChild(home_2)
var home_3 = document.createElement('li')
var link_3 = document.createElement('a')
link_3.setAttribute('href', '#')
link_3.textContent = 'Home 3'
home_3.appendChild(link_3)
subHome_list.appendChild(home_3)
li3.appendChild(subHome_list)
list.appendChild(li3)



sidebar.appendChild(list)
wrapper.appendChild(sidebar)


var content = document.createElement('div')
content.id = 'content'
var nav_ = document.createElement('nav')
nav_.setAttribute('class','navbar navbar-expand-lg navbar-light bg-light')
var container_fluid = document.createElement('div')
container_fluid.setAttribute('class','container-fluid')
var collapse_btn = document.createElement('button')
collapse_btn.setAttribute('type', 'button')
collapse_btn.setAttribute('id', '#sidebarCollapse')
collapse_btn.setAttribute('class', 'btn btn-info')
collapse_btn.setAttribute('onclick','toggle_sidebar()')
var i_vas = document.createElement('i')
i_vas.setAttribute('class', 'fas fa-home')
var span_toggle = document.createElement('span')
span_toggle.textContent='ToggleSidebar'
collapse_btn.appendChild(i_vas)
collapse_btn.appendChild(span_toggle)
//container_fluid.appendChild(collapse_btn)
nav_.appendChild(container_fluid)
content.appendChild(nav_)
wrapper.appendChild(content)


function toggle_sidebar() {

    var el = document.getElementById('sidebar')
    el.classList.toggle('active');

};