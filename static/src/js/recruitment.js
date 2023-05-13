odoo.define('smart_stock.recruitment', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');

    var _t = core._t;
    var QWeb = core.qweb;

    var RecruitmentWidget = Widget.extend({
        start: function () {
            this._loadJobs();
            this._bindEvents();
            return this._super.apply(this, arguments);
        },

        _bindEvents: function () {
            var self = this;
            setInterval(function () {
                self._loadJobs();
            }, 10000);
        },

        _loadJobs: function () {
            var self = this;
            ajax.jsonRpc('/job/recruitment', 'call', {}).then(function (data) {
                self.$('#jobs_container').html(QWeb.render('recruitment_job', {jobs: data.jobs}));
            });
        },
    });

    $(document).ready(function () {
        var recruitmentWidget = new RecruitmentWidget();
        recruitmentWidget.appendTo('#recruitment_widget');
    });

    return {
        RecruitmentWidget: RecruitmentWidget
    };
});
