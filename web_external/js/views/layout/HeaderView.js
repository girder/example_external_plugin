custom_app.views.LayoutHeaderView = custom_app.View.extend({
    events: {
    },

    render: function () {
        this.$el.html(custom_app.templates.layoutHeader());

        this.$('a[title]').tooltip({
            placement: 'bottom',
            delay: {show: 300}
        });

        new custom_app.views.LayoutHeaderUserView({
            el: this.$('.h-current-user-wrapper'),
            parentView: this
        }).render();
    }
});
