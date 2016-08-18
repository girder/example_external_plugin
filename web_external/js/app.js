custom_app.App = girder.App.extend({

    render: function () {
        this.$el.html(custom_app.templates.layout());

        new custom_app.views.LayoutHeaderView({
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
