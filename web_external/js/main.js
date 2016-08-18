$(function () {
    example_external_plugin.events.trigger('g:appload.before');
    example_external_plugin.mainApp = new example_external_plugin.App({
        el: 'body',
        parentView: null
    });
    example_external_plugin.events.trigger('g:appload.after');
});
