import datetime
from email.policy import default
from pyexpat import model
from re import U
from tokenize import String

from odoo import models, fields,api
from odoo.exceptions import UserError
import base64
import requests
import datetime

class purchaser(models.Model):
    _name = 'purchaser.company'
    purchase_individual = fields.Many2one(comodel_name='res.partner', string='Individual')
    purchase_company = fields.Many2one(comodel_name='res.company', string='Company')
    purchaser_id = fields.Many2one(comodel_name='sale.order')

class OLStartDate(models.Model):
    _inherit = 'sale.order'
    purchaser_ids = fields.One2many('purchaser.company','purchaser_id')




# select_purchase = fields.Selection([('purchase_1', 'Purchaser 1'), ('purchase_2', 'Purchaser 2'), ('purchase_3', 'Purchaser 3'), ('purchase_4', 'Purchaser 4')],
#                                                string='Select Purchase',
#                                                default='purchase_1')
    location = fields.Char(string='Location')
    location_arabic = fields.Char(string='Location Arabic')
    relevent_unit_no = fields.Many2one(comodel_name='product.product', string='Relevent Unit No')
    relevent_unit_area = fields.Char(string='Relevent Unit Area')
    relevent_bays_no = fields.Char(string='Relevent Bays No')

    bank_details = fields.Many2one(comodel_name='res.bank', string='Bank Details')
    anticipated_completion_date = fields.Date(string='Anticipated Completion Date')
    permitted_use = fields.Char(string='Permitted Use')
    permitted_use_arabic = fields.Char(string='Permitted Use(Arabic)')
    late_payment_fee = fields.Char(string='Late Payment Fee')
    late_payment_arabic = fields.Char(string='Late Payment Fee(Arabic)')
    down_payment = fields.Selection([('amount', 'Amount'), ('percentage', 'Percentage')],
                                                   string='Down Payment',
                                                   default='amount')
    amount = fields.Char(String='Amount')
    payment = fields.Selection([('monthly', 'Monthly'), ('quarterly', 'Quarterly'),('byannual', 'By Annual'), ('annual', 'Annual')],
                                                   default='monthly')
    start_date = fields.Date(String='Starting Date')
    end_date = fields.Date(String='Ending Date')
    percentage = fields.Float(String='Percentage')
    payment_duration = fields.Integer(String='Duration', default= 1)
    installment_amount = fields.Integer(String='Duration', compute = 'installmentamount')
    installment_payable_amount = fields.Float(String='Installment Payable Amount', compute='subtractioninamount')
    project = fields.Many2one('project.project', string='Project')
    # @api.depends('amount','amount_total')
    def subtractioninamount(self):
        if self.down_payment == "amount":
            self.installment_payable_amount = self.amount_total - float(self.amount)

        else:
            var = (self.percentage * self.amount_total)
            self.installment_payable_amount=self.amount_total-var
            print(self.installment_payable_amount)

    def installmentamount(self):
        self.installment_amount = self.installment_payable_amount / float(self.payment_duration)



class ContactInherit(models.Model):
    _inherit = 'res.partner'
    country_arabic = fields.Many2one(comodel_name='res.country', string='Nationality (Arabic)')
    passport_eng = fields.Char(string='Passport (English)')
    passport_arabic = fields.Char(string='Passport (Arabic)')
    fax_eng = fields.Char(string='Fax No (English)')
    fax_arabic = fields.Char(string='Fax No (Arabic)')
    street_arabic=fields.Char(String="Street (Arabic)")
    street2_arabic=fields.Char(String="street2 (Arabic)")
    zip_arabic=fields.Char(String="Zip(Arabic)")
    city_arabic=fields.Char(String="City (Arabic)")
    state_id_arabic = fields.Many2one(comodel_name='res.country.state', string='State')

class ContactInheritInCompany(models.Model):
    _inherit = 'res.company'
    country_arabic = fields.Many2one(comodel_name='res.country', string='Nationality (Arabic)')
    passport_eng = fields.Char(string='Passport (English)')
    passport_arabic = fields.Char(string='Passport (Arabic)')
    fax_eng = fields.Char(string='Fax No (English)')
    fax_arabic = fields.Char(string='Fax No (Arabic)')
    street_arabic=fields.Char(String="Street (Arabic)")
    street2_arabic=fields.Char(String="street2 (Arabic)")
    zip_arabic=fields.Char(String="Zip(Arabic)")
    city_arabic=fields.Char(String="City (Arabic)")
    registration_no=fields.Char(String="Registration No")
    state_id_arabic = fields.Many2one(comodel_name='res.country.state', string='State')

class inheritanceinbank(models.Model):
    _inherit = 'res.bank'


    account_no = fields.Char(String= 'Account Number')
    account_name = fields.Char(String= 'Account Name')
    IBAN = fields.Char(String='IBAN')
    swift = fields.Char(String='SWIFT')


