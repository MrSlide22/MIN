
class Operation
  include Mongoid::Document
  include Mongoid::Enum

  field :op, type: [:add, :div, :mult, :subs]
  field :op1, type: Integer
  field :op2, type: Integer
  field :t0, type: Time
  field :t1, type: Time
  field :estimation, type: String

  def total_time
    t1 - t0
  end

  def estimate
    self.estimation = HTTP.get("http://localhost:5000/predict/#{op1.to_f}/").to_s
  end

  def self.create_random
    @operation = Operation.new
    @operation.op1 = rand(10)
    @operation.op2 = rand(10)
    @operation.estimate
    @operation.t0 = Time.new
    @operation.save
  end
end
