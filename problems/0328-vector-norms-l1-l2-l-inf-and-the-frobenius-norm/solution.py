import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    match norm_type:
        case "l1":
            # Chuẩn entrywise L1: Tổng giá trị tuyệt đối của tất cả các phần tử
            return float(np.sum(np.abs(arr)))
            
        case "l2":
            # Chuẩn entrywise L2: Căn bậc hai của tổng bình phương tất cả các phần tử
            return float(np.sqrt(np.sum(np.square(arr))))
            
        case "linf":
            # Chuẩn entrywise L-infinity: Giá trị tuyệt đối lớn nhất trong các phần tử
            return float(np.max(np.abs(arr)))
            
        case "frobenius":
            # Kiểm tra bắt buộc mảng phải là 2D
            if arr.ndim != 2:
                raise ValueError("Frobenius norm requires a 2D array.")
            return float(np.linalg.norm(arr, ord='fro'))
            
        case _:
            raise ValueError(f"Unknown norm type: {norm_type}")
