# -*- coding: utf-8 -*-

from openerp import fields, models, _
from openerp.exceptions import UserError


class AccountPartnerLedger(models.TransientModel):
    _inherit = "account.report.partner.ledger"
    
    result_selection = fields.Selection([('customer', 'Receivable Accounts'),
                                        ( 'supplier', 'Payable Accounts' ),
                                        ( 'customer_supplier', 'Receivable and Payable Accounts' ),
                                        ( 'account.data_account_type_liquidity', 'Bank and Cash Accounts' ),
                                        ( 'account.data_account_type_current_assets', 'Current Assets' ),
                                        ( 'account.data_account_type_non_current_assets', 'Non-current Assets' ),
                                        ( 'account.data_account_type_fixed_assets', 'Fixed Assets' ),
                                        ( 'account.data_account_type_current_liabilities', 'Current Liabilities' ),
                                        ( 'account.data_account_type_non_current_liabilities', 'Non-current Liabilities' ),
                                        ( 'account.data_account_type_equity', 'Equity' ),
                                        ( 'account.data_account_type_revenue', 'Income' ),
                                        ( 'account.data_account_type_expenses', 'Expenses' ),
                                        ( 'account.data_account_type_depreciation', 'Depreciation' ),
                                        ( 'account.data_account_type_direct_costs', 'Cost of Revenue' )
                                        ], string="Partner's", required=True, default='customer')