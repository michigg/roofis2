module.exports = {
    presets: [
        '@vue/cli-plugin-babel/preset'
    ],
    "plugins": [ "istanbul" ],
    "env": {
        "test": {
            "plugins": [ "istanbul" ]
        }
    }
}
