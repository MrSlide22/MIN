class OperationsController < ApplicationController

    def initialize
        super
        @dev = true
    end

    def index
        if not @dev
            redirect_to "/operations/answer"
        end
        @operations = Operation.all
    end

    def show
        if not @dev
            redirect_to "/operations/answer"
        end
        @operation = Operation.find(params[:id])
    end

    def new
        if not @dev
            redirect_to "/operations/answer"
        end
        @operation = Operation.new
    end

    def create
        if not @dev
            redirect_to "/operations/answer"
        end
        @operation = Operation.new

        @operation.op1 = params[:operation][:op1]
        @operation.op2 = params[:operation][:op2]
        @operation.operator = params[:operation][:operator]

        result = @operation.op1.send(@operation.operator, @operation.op2.to_f)
        p result
        if result != result.to_i
            @error = "Error. Result " + result.to_s + " is not an integer"
            redirect_to "/operations/new?error="+@error.to_s
        else
            @operation.save
            redirect_to "/operations/new?error=false"
        end
    end

    def destroy
        if not @dev
            redirect_to "/operations/answer"
        end
        operation = Operation.find(params[:id])
        operation.destroy
        redirect_to "/operations"
    end

    def resetTime
        operation = Operation.find(params[:id])
        operation.response_time = nil
        operation.save

        redirect_to '/operations'
    end

    def answer
        @operation = Operation.where(response_time: nil).take
    end

    def submitAnswer

        @operation = Operation.find(params[:id])
        @result = params[:result]

        correctresult = @operation.op1.send(@operation.operator, @operation.op2)
        p @result

        if correctresult.to_i == @result.to_i

            init_time = params[:init_time].to_i
            end_time = params[:end_time].to_i
            @operation.response_time = end_time - init_time
            @operation.save

            redirect_to "/operations/answer?error=false"

        else

            @error = "Wrong result"
            redirect_to "/operations/answer?error="+@error.to_s
        end
    end

    def add
        if not @dev
            redirect_to "/operations/answer"
        end
        number = params[:num]

        operators = ['+', '-', '*', '/']

        for i in 1..number.to_i

            @operation = Operation.new

            loop do
                @operation.op1 = rand(100)
                @operation.op2 = rand(100)
                @operation.operator = operators[rand(4)]

                if @operation.operator != '/' and @operation.op2 != 0
                    result = @operation.op1.send(@operation.operator, @operation.op2.to_f)
                end

                break if result == result.to_i
            end

            @operation.save
        end

        redirect_to "/?error=false"
    end

    def removeAll
        Operation.destroy_all
        redirect_to "/?error=false"
    end
end
