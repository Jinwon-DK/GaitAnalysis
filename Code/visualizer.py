import Code.viz_collector as viz
from Code.utils import dt_printer as dt


def chosen_viz(param, datasets):
    if param.method == "extended":
        print(f"{dt()} :: --{param.method} Selected")
        return viz.method_extend(param, datasets)
    elif param.object == "custom":
        print(f"{dt()} :: --{param.object} Selected")
        return viz.method_create(param, datasets)
    elif param.method == "normalized":
        print(f"{dt()} :: --{param.object} Selected")
        return viz.method_normalized(param, datasets)


