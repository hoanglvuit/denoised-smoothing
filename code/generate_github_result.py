from analyze import plot_certified_accuracy_per_sigma_best_model, Line, ApproximateAccuracy

certification_result_with_denoiser = "/kaggle/working/certification_output/sigma_0.12"
certification_result_without_denoiser = "/kaggle/working/certification_output/sigma_0.12"

plot_certified_accuracy_per_sigma_best_model(
    "/kaggle/working/sigma012", 'With vs Without Denoiser', 1.5,
    methods=
        [Line(ApproximateAccuracy(certification_result_with_denoiser), "$\sigma = 0.12$")],
    label='With Denoiser',
    methods_base=
        [Line(ApproximateAccuracy(certification_result_without_denoiser), "$\sigma = 0.12$")], 
    label_base='Without Denoiser',
    sigmas=[0.12])


certification_result_with_denoiser = "/kaggle/working/certification_output/sigma_0.25"
certification_result_without_denoiser = "/kaggle/working/certification_output/sigma_0.25"

plot_certified_accuracy_per_sigma_best_model(
    "/kaggle/working/sigma025", 'With vs Without Denoiser', 1.5,
    methods=
        [Line(ApproximateAccuracy(certification_result_with_denoiser), "$\sigma = 0.25$")],
    label='With Denoiser',
    methods_base=
        [Line(ApproximateAccuracy(certification_result_without_denoiser), "$\sigma = 0.25$")], 
    label_base='Without Denoiser',
    sigmas=[0.25])



certification_result_with_denoiser = "/kaggle/working/certification_output/sigma_0.50"
certification_result_without_denoiser = "/kaggle/working/certification_output/sigma_0.50"

plot_certified_accuracy_per_sigma_best_model(
    "/kaggle/working/sigma05", 'With vs Without Denoiser', 1.5,
    methods=
        [Line(ApproximateAccuracy(certification_result_with_denoiser), "$\sigma = 0.50$")],
    label='With Denoiser',
    methods_base=
        [Line(ApproximateAccuracy(certification_result_without_denoiser), "$\sigma = 0.50$")], 
    label_base='Without Denoiser',
    sigmas=[0.50])


certification_result_with_denoiser = "/kaggle/working/certification_output/sigma_1.00"
certification_result_without_denoiser = "/kaggle/working/certification_output/sigma_1.00"

plot_certified_accuracy_per_sigma_best_model(
    "/kaggle/working/sigma1", 'With vs Without Denoiser', 1.5,
    methods=
        [Line(ApproximateAccuracy(certification_result_with_denoiser), "$\sigma = 1.00$")],
    label='With Denoiser',
    methods_base=
        [Line(ApproximateAccuracy(certification_result_without_denoiser), "$\sigma = 1.00$")], 
    label_base='Without Denoiser',
    sigmas=[1.00])