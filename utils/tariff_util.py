def response_tariffs_of_distributor(start_date, end_date, pending, blue_tariff, green_tariff):
    response = {
        "start_date": start_date,
        "end_date": end_date,
        "overdue": pending,
        "blue": {
            "peakTusdInReaisPerKw": blue_tariff.peak_tusd_in_reais_per_kw,
            "peakTusdInReaisPerMwh": blue_tariff.peak_tusd_in_reais_per_mwh,
            "peakTeInReaisPerMwh": blue_tariff.peak_te_in_reais_per_mwh,
            "offPeakTusdInReaisPerKw": blue_tariff.off_peak_tusd_in_reais_per_kw,
            "offPeakTusdInReaisPerMwh": blue_tariff.off_peak_tusd_in_reais_per_mwh,
            "offPeakTeInReaisPerMwh": blue_tariff.off_peak_te_in_reais_per_mwh,
        },
        "green": {
            "peakTusdInReaisPerMwh": green_tariff.peak_tusd_in_reais_per_mwh,
            "peakTeInReaisPerMwh": green_tariff.peak_te_in_reais_per_mwh,
            "offPeakTusdInReaisPerMwh": green_tariff.off_peak_tusd_in_reais_per_mwh,
            "offPeakTeInReaisPerMwh": green_tariff.off_peak_te_in_reais_per_mwh,
            "naTusdInReaisPerKw": green_tariff.na_tusd_in_reais_per_kw,
        }
    }

    return response