import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Multiselect from 'vue-multiselect'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import VueI18n from 'vue-i18n'


Vue.use(VueI18n);

function loadLocaleMessages() {
    const locales = require.context(
        "./locales",
        true,
        /[A-Za-z0-9-_,\s]+\.json$/i
    );
    const messages = {};
    locales.keys().forEach(key => {
        const matched = key.match(/([A-Za-z0-9-_]+)\./i);
        if (matched && matched.length > 1) {
            const locale = matched[1];
            messages[locale] = locales(key);
        }
    });
    return messages;
}

const i18n = new VueI18n({
    locale: navigator.language.split('-')[0],
    fallbackLocale: process.env.VUE_APP_I18N_FALLBACK_LOCALE || "de",
    messages: loadLocaleMessages()
});

function getLocaleIDs() {
    let locales = require.context(
        "./locales",
        true,
        /[A-Za-z0-9-_,\s]+\.json$/i
    );
    let localeIds = [];
    for (const key of locales.keys()) {
        const matched = key.match(/([A-Za-z0-9-_]+)\./i);
        if (matched && matched.length > 1) {
            const locale = matched[1];
            localeIds.push(locale)
        }
    }
    return localeIds;
}

const getRuntimeConfig = async () => {
    const runtimeConfig = await fetch('/config/config.json');
    return await runtimeConfig.json()
};
getRuntimeConfig().then(function (json) {
    Vue.mixin({
        data() {
            return {
                VERSION: "1.2.0",
                ROOFIS_API: json.ROOFIS_API,
                LECTOR_BUILDING_API: json.LECTOR_BUILDING_API,
                LECTOR_WEB_URL: json.LECTOR_WEB_URL,
                UNI_INFO_API: json.UNI_INFO_API,
                IMPRINT_DATA: json.IMPRINT_DATA,
                PRIVACY_DATA: json.PRIVACY_DATA,
            }
        },
    });

    Vue.prototype.$locales = getLocaleIDs();

    axios.defaults.headers = {'Access-Control-Allow-Origin': '*'};
    Vue.use(VueAxios, axios);
    Vue.use(BootstrapVue);
    Vue.use(IconsPlugin);
    Vue.component('multiselect', Multiselect);

    Vue.config.productionTip = false;

    new Vue({
        i18n,
        router,
        render: h => h(App),
    }).$mount('#app');
});



