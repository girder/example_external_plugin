var example_external_plugin = example_external_plugin || {};

_.extend(example_external_plugin, {
    models: {},
    collections: {},
    views: {},
    router: new Backbone.Router(),
    events: _.clone(Backbone.Events)
});

girder.router.enabled(false);
