class CreateOperations < ActiveRecord::Migration
  def change
    create_table :operations do |t|
      t.integer :op1
      t.string  :op
      t.integer :op2
      t.float :time

      t.timestamps null: false
    end
    change_column :operations, :time, :decimal
  end
end
