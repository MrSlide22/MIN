class OperationsController < ApplicationController
   def index
      @operations = Operation.all
   end

   def new
      @operation = Operation.new
      create
   end

   def create
      @operation.op = ['+', 'x', '-', '/'].shuffle[0]
      @operation.op1 = Random.rand(100)
      @operation.op2 = Random.rand(1..100)
      @operation.time = 0

      @operation.save
      redirect_to @operation
   end
	
   def show
      @operation = Operation.find(params[:id])
   end

   def answer
      @operation = Operation.find(params[:id])
      op = @operation.op
      if op == '+'
         correct = @operation.op1 + @operation.op2
      elsif op == '-'
         correct = @operation.op1 - @operation.op2
      elsif op == 'x'
         correct = @operation.op1 * @operation.op2
      elsif op == '/'
         correct = @operation.op1 / @operation.op2
      end
      if params[:answer].to_i == correct
         @correct = true
         @operation.time = (params[:end_time].to_f - params[:init_time].to_f).fdiv(1000)
         @operation.save
      else
         @correct = false
      end
   end
   
   def export
	require 'csv'
        CSV.open('operations.csv', 'w') do |csv|
           csv << Operation.column_names
           Operation.all.each do |o|
              csv << o.attributes.values
           end
        end
   end

   private
   def operation_params
      params.require(:operation).permit(:id, :op1, :op, :op2)
   end
end
