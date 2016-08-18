example_external_plugin.App = girder.App.extend({

    render: function () {
        this.$el.html(example_external_plugin.templates.layout());

        new example_external_plugin.views.LayoutHeaderView({
            el: this.$('#c-app-header-container'),
            parentView: this
        }).render();

        return this;
    },

    navigateTo: function (view, settings) {
        this.$('#g-app-body-container').removeClass('c-body-nopad');
        return girder.App.prototype.navigateTo.apply(this, arguments);
    }
});
