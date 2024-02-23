window.onload = function () {
    $("#search_result").modal("toggle");
};

function confirmPay() {
    fetch("/api/nurse/payment", {
        method: "post",
        body: JSON.stringify({
            medical_examination_id: $("#medical_examination_id_pay").text(),
        }),
        headers: {
            "Content-Type": "application/json",
        },
    }).then(function (res) {
        return res.json();
    }).then(function (datas) {
        if (datas["result"]) {
            Swal.fire({
                title: 'Thanh toán thành công',
                text: 'Đã xuất phiếu khám',
                icon: 'success',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok',
            })
            exportPDF();
            resetData();
            return;
        }
        Swal.fire({
            title: 'Thanh toán thất bại',
            text: 'Vui lòng kiểm tra lại',
            icon: 'error',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Ok',
        })
    });
}

function resetData() {
    $("#bill_detail").hide();
}

function exportPDF() {
    var today = new Date();
    var date = today.getDate() + '/' + (today.getMonth() + 1) + '/' + today.getFullYear();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var dateTime = date + ' ' + time;
    const pdf = new jsPDF({
        encodings: "utf-8",
        orientation: "portrait",
        format: "a4",
        putOnlyUsedFonts: true,
        floatPrecision: 16,
    });
    pdf.setFontSize(13);
    pdf.setFont('times')
    pdf.text(`Phong kham da khoa Ngan Thuong`, 20, 10)
    pdf.text(`Dia chi: Thi xa Dong Van, huyen Duy Tien, tinh Ha Nam`, 20, 20)
    pdf.text(`Dien thoai: 035 902 1176`, 20, 30)
    pdf.text("HOA DON THANH TOAN", 77, 50);
    fullname = $("#customer_fullname_pay").text().replaceAll('\n', '').trim().split(' ');

    pdf.text(`Ho Ten: ${fullname[0]} ${fullname[fullname.length-1]}`, 20, 70)
    pdf.text(`Ngày khám: ${dateTime}`, 110, 110)
    pdf.text(`Tien kham: ${$("#medical_examination_price_pay").text()}`, 20, 80);
    pdf.text(`Tien thuoc: ${$("#medicine_price_total_pay").text()}`, 110, 80);
    pdf.text(`Tong tien: ${$("#total_price_pay").text()}`, 20, 90);
    pdf.text(`Y ta thanh toan`, 120, 120)
    pdf.text(`(Ki, ghi ro ho ten, dong dau)`, 110, 130)

    pdf.autoPrint({
        variant: "non-conform",
    });
    pdf.save("medical bill.pdf");
}

$(document).ready(function () {
    $("#confirm").click(function () {
        confirmPay();
    });
});