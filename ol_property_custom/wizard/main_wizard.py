import datetime
from re import U

from odoo import models, fields,api
from odoo.exceptions import UserError
import base64
import requests
import datetime



class CreatBuilding(models.TransientModel):
    _name = "create.building.wizard"
    
    no_of_building = fields.Integer("No of Buildings")
    

    def create_building(self):
        active_id = self._context.get('active_id')
        no = self._context['no_of_build']
        obj = self.env['property.building'].search([('project_id','=',active_id)])
        obj_project=self.env['project.project'].search([('id','=',active_id)])
        for i in range(no):

            if obj:
                self.env['property.building'].create({
                    'project_id':active_id,
                        'code': obj_project.code+"-"+f'{len(obj.ids)+1+i:02}'
                })
            else:
                self.env['property.building'].create({
                    'project_id':active_id,
                        'code': obj_project.code+"-"+f'{i+1:02}'
                })
        
        

# create floor
class CreatFloor(models.TransientModel):
    _name = "create.floor.wizard"
    
    no_of_floor = fields.Integer("No of Floors")
    

    def create_floor(self):
        active_id = self._context.get('active_id')
        no = self._context['floor']
        obj = self.env['property.floor'].search([('id','=',active_id)])
        
        obj_project = self.env['property.building'].search([('id','=',active_id)])
        for i in range(no):

            if obj:
                self.env['property.floor'].create({
                    'building_id':active_id,
                    'code': obj_project.code+"-"+f'{len(obj.ids)+1+i:02}'
                })
            else:
                self.env['property.floor'].create({
                    'building_id':active_id,
                        'code': obj_project.code+"-"+f'{i+1:02}'
                })


# create units
class CreatUnits(models.TransientModel):
    _name = "create.units.wizard"
    
    no_of_unit = fields.Integer("No of Units")
    

    def create_units(self):
        active_id = self._context.get('active_id')
        no = self._context['units']
        obj = self.env['product.product'].search([('floor_id','=',active_id)])
        
        obj_project = self.env['property.floor'].search([('id','=',active_id)])
        for i in range(no):
            if obj:
                self.env['product.product'].create({
                    'name':obj_project.code+"-"+f'{len(obj.ids)+1+i:02}',
                    'floor_id':active_id
                })
            else:
                self.env['product.product'].create({
                    'name':obj_project.code+"-"+f'{i+1:02}',
                     'floor_id':active_id
                })