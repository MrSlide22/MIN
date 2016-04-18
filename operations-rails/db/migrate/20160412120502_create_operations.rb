class CreateOperations < ActiveRecord::Migration
  def change
    create_table :operations do |t|
      t.integer :op1
      t.integer :op2
      t.text :operator
      t.time :response_time

      t.timestamps null: false
    end
  end
end
