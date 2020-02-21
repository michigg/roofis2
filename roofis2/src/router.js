import Vue from 'vue'
import Router from 'vue-router'
import Roofis2 from "./views/Roofis2";
import Imprint from "./views/Imprint";
import Privacy from "./views/Privacy";

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Roofis2',
            component: Roofis2
        },
        {
            path: '/imprint',
            name: 'imprint',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: Imprint
        },
        {
            path: '/privacy',
            name: 'privacy',
            component: Privacy
        },
    ]
})
