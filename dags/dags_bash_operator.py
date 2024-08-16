from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # deck 이름(deck 파일명과 동일시하기)
    schedule="0 0 * * *", # cron schedule 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),  
    catchup=False, # False : 사이 누락된 구간 실행 x
    # dagrun_timeout=datetime.timedelta(minutes=60), # timeout 실행
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1", # task랑 동일하게 맞춰주기
        bash_command="echo whoami", # 명령어
    )

    bash_t2 = BashOperator(
        task_id="bash_t2", # task랑 동일하게 맞춰주기
        bash_command="echo $HOSTNAME", # 명령어
    )

    # 실행 순서
    bash_t1 >> bash_t2