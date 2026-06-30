from prefect import flow, task
import subprocess

@task(name="Ingesta con Polars")
def tarea_ingesta():
    subprocess.run(["python", "src/ingest.py"], check=True)

@task(name="Transformación dbt")
def tarea_dbt():
    subprocess.run(["dbt", "run", "--project-dir", "./dbt"], check=True)

@flow(name="Pipeline Ecommerce")
def pipeline_flow():
    tarea_ingesta()
    tarea_dbt()

if __name__ == "__main__":
    pipeline_flow()
