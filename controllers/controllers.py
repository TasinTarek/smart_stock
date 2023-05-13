import random
from odoo import http, _
from odoo.http import request


class MyController(http.Controller):
    @http.route('/job/recruitment', type='http', auth='user', website=True)
    def my_job_route(self, **kw):
        jobs = http.request.env['hr.job'].search(
            [], order='create_date desc', limit=10)
        # Shuffle the jobs
        shuffled_jobs = list(jobs)
        random.shuffle(shuffled_jobs)

        # Show only 4 random jobs
        num_jobs_to_show = min(4, len(shuffled_jobs))
        shuffled_jobs = shuffled_jobs[:num_jobs_to_show]
        return http.request.render("smart_stock.recruitment_job", {
            'jobs': shuffled_jobs,
        })
