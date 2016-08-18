example_external_plugin.views.LayoutHeaderView = example_external_plugin.View.extend({
    events: {
    },

    render: function () {
        this.$el.html(example_external_plugin.templates.layoutHeader());

        this.$('a[title]').tooltip({
            placement: 'bottom',
            delay: {show: 300}
        });

        new example_external_plugin.views.LayoutHeaderUserView({
            el: this.$('.h-current-user-wrapper'),
            parentView: this
        }).render();
    }
});
