# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
Operation.create!(op1: 1, op2: 2, operator: '+', response_time: 0)
Operation.create!(op1: 3, op2: 4, operator: '*', response_time: 0)
Operation.create!(op1: 1, op2: 2, operator: '+', response_time: 0)
Operation.create!(op1: 1, op2: 2, operator: '+', response_time: 0)
