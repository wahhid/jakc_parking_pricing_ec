from openerp.osv import fields, osv
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


AVAILABLE_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('done','Close'),
]

class park_pricing(osv.osv):
    _name = "park.pricing"
    _description = "Parking Pricing"
    _columns = {
        'name': fields.char('Name', size=100, required=True),
        'vehicle_type_id' : fields.many2one('park.vehicle.type', 'Vehicle Type', required=True),                
        'limit_time_charge':  fields.integer('Limit Time for Charge (minutes)', required=True),            
        'first_hours_charge': fields.float('First Hours Charge'),
        'second_hours_charge': fields.float('Second Hours Charge'),
        'third_hours_charge': fields.float('Third Hours Charge'),
        'next_hours_charge': fields.float('Next Hours Charge'),
        'service_charge': fields.float('Service Charge'),
        'pinalty_charge': fields.float('Pinalty Charge'), 
        'is_voucher_allowed': fields.boolean('Voucher Allowed'),                 
        'state': fields.selection(AVAILABLE_STATES,'Status',size=16,readonly=True,required=True),        
    }
    _defaults = {
        'limit_time_charge': lambda *a: 0,
        'state': lambda *a: 'open',
    }
park_pricing()