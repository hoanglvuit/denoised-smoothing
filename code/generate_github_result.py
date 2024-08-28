from analyze import plot_certified_accuracy_per_sigma_best_model, Line, ApproximateAccuracy

certification_result_with_denoiser = "/kaggle/working/certification_output/sigma_0.25"
certification_result_without_denoiser = "/kaggle/working/certification_output/sigma_0.25"

plot_certified_accuracy_per_sigma_best_model(
    "/kaggle/working/certification_output", 'With vs Without Denoiser', 1.0,
    methods=
        [Line(ApproximateAccuracy(certification_result_with_denoiser), "$\sigma = 0.12$")],
    label='With Denoiser',
    methods_base=
        [Line(ApproximateAccuracy(certification_result_without_denoiser), "$\sigma = 0.12$")], 
    label_base='Without Denoiser',
    sigmas=[0.25])
