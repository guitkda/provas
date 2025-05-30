from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

default_args = {'start_date': datetime(2024, 1, 1)}
dag = DAG('pipeline_meteorologia', schedule_interval=None, default_args=default_args, catchup=False)

def unificar(): os.system('python /opt/airflow/scripts/unificar_csvs.py')
def grafico(): os.system('python /opt/airflow/scripts/gerar_grafico.py')

t1 = PythonOperator(task_id='unificar_dados', python_callable=unificar, dag=dag)
t2 = PythonOperator(task_id='gerar_grafico', python_callable=grafico, dag=dag)

t1 >> t2