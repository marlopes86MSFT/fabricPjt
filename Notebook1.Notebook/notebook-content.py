# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


#test
%%pyspark
import sempy.fabric as fabric 

workspace_name = None #None if you want to use the current workspace
#if None, use current workspace otherwise the specified workspace
wsid = fabric.get_workspace_id() if workspace_name is None else fabric.resolve_workspace_id(workspace_name) 

#You can make below dynamic as well
lh_name = "lsgit1"

#create variables to use in scala
spark.conf.set("ws_id", wsid)
spark.conf.set("lh_name",lh_name)



%%spark

import com.microsoft.spark.fabric.tds.implicits.read

import com.microsoft.spark.fabric.Constants

val t_sql_query = """
-- YOUR T-SQL 
select 1

"""

#val wsid = spark.conf.get("ws_id")
#val lh_name = spark.conf.get("lh_name")

val df  = spark.read.option(Constants.WorkspaceId, wsid).option(Constants.DatabaseName, lh_name).synapsesql(t_sql_query)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
