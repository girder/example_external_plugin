$(function () {
    custom_app.events.trigger('g:appload.before');
    custom_app.mainApp = new custom_app.App({
        el: 'body',
        parentView: null
    });
    custom_app.events.trigger('g:appload.after');
});
